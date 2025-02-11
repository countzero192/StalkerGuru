import requests
import pickle
from time import sleep
import random
import os
from string import ascii_letters
import shutil

ALPHA = ascii_letters + "0123456789"
BASEURL = "https://i.imgur.com"
HEADERS = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0"
}

used = []
if os.path.exists("save"):
    with open("save", 'rb') as file:
        used = pickle.load(file)
if not os.path.exists("images"):
    os.mkdir("images")


def gen_name() -> str:
    EXT = "jpeg"
    name = ''.join([random.choice(ALPHA) for _ in range(7)])
    name = f"{name}.{EXT}"
    while name in used:
        name = ''.join([random.choice(ALPHA) for _ in range(7)])
        name = f"{name}.{EXT}"
    used.append(name)
    return name


def download() -> None:
    file = gen_name()
    url = f"{BASEURL}/{file}"
    with requests.get(url, stream=True, headers=HEADERS) as req:
        if (req.status_code == 200) and ("removed" not in req.url):
            print(f"[Downloading to images/{file}]")
            with open(f"images/{file}", 'wb') as file:
                shutil.copyfileobj(req.raw, file)


def main():
    try:
        while True:
            sleep(random.random())
            download()
    except KeyboardInterrupt:
        return
    finally:
        with open("save", "wb") as f:
            pickle.dump(used, f)
        print("Progress saved in ./save")


if __name__ == "__main__":
    print("StalkerGuru by countzero192")
    main()

