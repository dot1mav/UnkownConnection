import requests
import os

from tqdm import tqdm
from bs4 import BeautifulSoup
from typing import AnyStr


class Proxy(object):
    __doc__ = " This class made to build and check and change proxy list "
    __proxies: dict = dict()
    __site_url: str = None

    def __init__(self) -> None:
        if self.__site_url is None:
            self.__GetSiteUrl()
            self._GetProxy()
        else:
            self.__GetProxy()

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
                if len(cols) != 0:
                    print(cols[0])
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
        import random
        random.seed(4096)
        check: int = 0
        for i in range(4):
            temp: int = random.randint(0, max(self.__proxies.keys()))
            print(f'{self.__proxies[temp].get("ip")}')
            if self.__CheckConnection(self.__proxies[temp].get('ip')):
                check += 1
            else:
                self.__proxies.pop(temp)

        del random

        if check <= 3:
            self.__MakeItBetter()

    def __CheckConnection(self, host: AnyStr) -> bool:
        exit_code = os.system(f"ping -c 1 -w2 {host} > /dev/null 2>&1")
        if exit_code == 0:
            return True
        else:
            return False

    def __call__(self, *args, **kwargs) -> None:
        pass

    def __repr__(self) -> str:
        del self.__proxies
        del self.__site_url

    def __del__(self) -> None:
        pass

    def __sizeof__(self) -> int:
        return len(self.__proxies)

    def __iter__(self) -> dict:
        pass

    def __str__(self) -> str:
        return " ".join(self.__proxies[ke] for ke in self.__proxies.keys())
