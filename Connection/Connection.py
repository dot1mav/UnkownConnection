import os
import socket
import requests

from typing import Any

from .Proxy import ProxyList


class Connection(object):
    __local_ip: str = None
    __proxy: str = None

    def __init__(self) -> None:
        self._proxy: ProxyList = ProxyList()
        self.__local_ip = self.__CheckIP()

    @staticmethod
    def __CheckIP() -> str:
        return requests.get("https://api.ipify.org/").text

    def __str__(self) -> str:
        return f'''local -> {self.__local_ip}
proxy number 1 -> {self.__proxy}'''
