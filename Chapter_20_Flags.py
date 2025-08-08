import time
from pathlib import Path
from typing import Callable
import httpx

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'https://www.fluentpython.com/data/flags'
DEST_DIR = Path('downloaded')

def save_flag(img: bytes, filename: str):
    (DEST_DIR / filename).write_bytes(img)

def get_flag(cc: str) -> bytes:
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = httpx.get(url, timeout=6.0, follow_redirects=True)
    resp.raise_for_status()
    return resp.content

def download_many(cc_list: list[str]):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        save_flag(image, cc.lower() + '.gif')
        print(cc, end=' ', flush=True)
    return len(cc_list)

def main(downloader: Callable):
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.time()
    count = downloader(POP20_CC)
    t1 = time.time()
    print(count, 'flags downloaded in', round(t1 - t0, 2), 'seconds')

if __name__ == '__main__':
    main(download_many)