import os
import requests
import random

from typing import Any

from .Proxy import ProxyList


class Connection(object):
    __local_ip: str = None
    __proxy: str = None

    def __init__(self) -> None:
        self._proxy: ProxyList = ProxyList()
        self.__local_ip = self.__CheckIP()

    def connect(self) -> None:
        temp_int: int = random.randint(0, max(self._proxy._proxies_use.keys()))
        self.__proxy = f'https://{self._proxy._proxies_use[temp_int]["ip"]}:{self._proxy._proxies_use[temp_int]["port"]}'
        os.environ['https_proxy'] = self.__proxy
        os.environ['HTTPS_PROXY'] = self.__proxy
        print(f'now connect to {self.__CheckIP()}')

    @staticmethod
    def __CheckIP() -> str:
        return requests.get("https://api.ipify.org/").text

    def __str__(self) -> str:
        return f'''local -> {self.__local_ip}
proxy number 1 -> {self.__proxy}'''
