import os
import requests
import platform

from bs4 import BeautifulSoup
from requests.models import Response




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


def get_proxies() -> list:
    site: str = 'https://free-proxy-list.net/anonymous-proxy.html'
    hdr: dict = {'User-Agent': 'Mozilla/5.0'}
    req = requests.get(site)
    html = BeautifulSoup(req.text, "lxml")
    rows = html.findAll("tr")
    proxies: list = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text for ele in cols]
        try:
            print(f'{cols}')
            ipaddr = cols[0]
            portNum = cols[1]
            proxy = ipaddr+":"+portNum
            portName = cols[6]
            if portName == "no":
                pass
            else:
                proxies.append(str(proxy))
        except:
            pass
    return proxies


if __name__ == "__main__":
    proxy_list: list = get_proxies()
    for proxy in proxy_list:
        print(f'{proxy}')