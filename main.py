import os
import bs4
import requests

from bs4 import BeautifulSoup


def get_proxies():
    site = 'https://free-proxy-list.net/anonymous-proxy.html'
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = requests.get(site)
    html = BeautifulSoup(req.text, "lxml")
    rows = html.findAll("tr")
    proxies = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text for ele in cols]
        try:
            ipaddr = cols[0]  # ipAddress
            portNum = cols[1]  # portNum
            proxy = ipaddr+":"+portNum  # concatinating
            portName = cols[6]  # portName variable yes / No
            if portName == "no":
                pass  # proxies.append(str(proxy))
            else:
                # if portNum=='80' or portNum=='8080':
                proxies.append(str(proxy))
        except:
            pass
    return proxies


if __name__ == "__main__":
    proxy_list: list = get_proxies()
    for proxy in proxy_list:
        print(f'{proxy}')