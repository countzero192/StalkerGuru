from time import sleep
import requests
from typing import List

with open("http.txt", 'r') as file:
    proxies = [i.strip() for i in file]
test_url = "https://archlinux.org"


def test_proxy(addr: str) -> bool:
    try:
        p = {"http": addr}
        r = requests.get(test_url, proxies=p)
        if r.status_code == 200:
            return True
        else:
            return False
    except Exception as E:
        print(E)
    return True


def get_proxy(verbose: bool = False) -> List[str]:
    global proxies
    if verbose:
        print("[Getting working proxies]")
    proxies = list(filter(test_proxy, proxies[:100]))
    return proxies

