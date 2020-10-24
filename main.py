import os
import requests
import platform

from bs4 import BeautifulSoup
from tqdm import tqdm


def ping(host: str) -> bool:
    current_os = platform.system().lower()
    if current_os == "windows":
        parameter = "-n"
    else:
        parameter = "-c"
    exit_code = os.system(f"ping {parameter} 1 -w2 {host} > /dev/null 2>&1")
    if exit_code == 0:
        return True
    else:
        return False


def get_proxies() -> dict:
    site: str = 'https://free-proxy-list.net/anonymous-proxy.html'
    hdr: dict = {'User-Agent': 'Mozilla/5.0'}
    req = requests.get(site)
    html = BeautifulSoup(req.text, "lxml")
    rows = html.findAll("tr")
    proxies: dict = dict()
    counter: int = 0
    for row in tqdm(rows, desc='Make proxy list...'):
        cols = row.find_all('td')
        cols = [ele.text for ele in cols]
        try:
            if ping(cols[0]) and len(cols) != 0:
                proxies[counter] = {
                    'ip': cols[0],
                    'port': cols[1],
                    'ZIP': cols[2],
                    'type': cols[4]
                }
                counter += 1
        except:
            pass
    return proxies


if __name__ == "__main__":
    proxy_list: dict = get_proxies()
    print(f'{proxy_list}')
    for proxy in proxy_list.keys():
        print(f'{proxy_list[proxy]}')
