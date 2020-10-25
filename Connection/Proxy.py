import requests
import os
import random

from tqdm import tqdm
from bs4 import BeautifulSoup
from typing import AnyStr, Any


class ProxyServer(object):
    def __init__(self) -> None:
        pass


class ProxyList(object):
    __doc__ = " This class made to build and check and change proxy list "
    __proxies: dict = dict()
    _proxies_use: dict = dict()
    __site_url: str = None

    def __init__(self) -> None:
        if self.__site_url is None:
            self.__GetSiteUrl()
            self._GetProxy()
        else:
            self._GetProxy()

        self.__MakeItBetter()

    def _GetProxy(self) -> None:
        hdr: dict = {'User-Agent': 'Mozilla/5.0'}
        req = requests.get(self.__site_url)
        html = BeautifulSoup(req.text, "lxml")
        rows = html.findAll("tr")
        counter: int = 0
        for row in tqdm(rows, desc='Make proxy list...'):
            cols = row.find_all('td')
            cols = [ele.text for ele in cols]
            try:
                if len(cols) != 0 and self.__ValidateIp(cols[0]):
                    self.__proxies[counter] = {
                        'ip': cols[0],
                        'port': cols[1],
                        'ZIP': cols[2],
                        'type': cols[4]
                    }
                    counter += 1
            except:
                pass

    def _ChangeProxy(self) -> None:
        pass

    def __GetSiteUrl(self):
        self.__site_url = 'https://free-proxy-list.net/'

    def __MakeItBetter(self) -> None:
        if len(self._proxies_use.keys()) != 0:
            self._proxies_use.clear()
        random.seed(4096)
        counter: int = 0
        temp: int = 0
        for _ in range(10):
            temp = random.randint(0, max(self.__proxies.keys()))
            if self.__CheckConnection(self.__proxies[temp].get('ip')):
                self._proxies_use[counter] = self.__proxies[temp]
                counter += 1
        if len(self._proxies_use.keys()) <= 3:
            self.__MakeItBetter()

    def __CheckConnection(self, host: AnyStr) -> bool:
        exit_code = os.system(f"ping -c 1 -w2 {host} > /dev/null 2>&1")
        if exit_code == 0:
            return True
        else:
            return False

    def __ValidateIp(self, ip) -> bool:
        ip_part = ip.split('.')
        if len(ip_part) != 4:
            return False
        for x in ip_part:
            if not x.isdigit():
                return False
            i = int(x)
            if i < 0 or i > 255:
                return False
        return True

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __del__(self) -> None:
        self.__proxies = None
        self._proxies_use = None
        self.__site_url = None

    def __sizeof__(self) -> int:
        return len(self.__proxies)

    def __iter__(self) -> dict:
        pass

    def __str__(self) -> str:
        return "\n".join(str(self._proxies_use[ke]) for ke in self._proxies_use.keys())
