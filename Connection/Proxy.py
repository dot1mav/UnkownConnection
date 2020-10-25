import requests

from bs4 import BeautifulSoup


class Proxy(object):

  # attributes
  __doc__ = " This class made to build and check and change proxy list "
  __proxies: dict = dict()

   def __init__(self) -> None:
        pass

    # protected methods

    def _GetProxy() -> dict:
        pass

    def _ChangeProxy() -> dict:
        pass

    # private mthods

    def __CheckConnection(host: str) -> bool:
        pass
