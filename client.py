from curl_cffi import requests
import random
import time

BASE = "https://bankrot.fedresurs.ru/backend"

UA_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0 Safari/537.36",
]

def get_bankrot(path, params=None):
    url = BASE + path

    headers = {
        "User-Agent": random.choice(UA_LIST),
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://bankrot.fedresurs.ru/",
        "Origin": "https://bankrot.fedresurs.ru",
        "Accept-Language": "ru-RU,ru;q=0.9",
        "Connection": "keep-alive",
    }

    session = requests.Session()
    session.impersonate = "chrome120"   # 🔥 КРИТИЧНО

    r = session.get(url, params=params, headers=headers, timeout=20)

    print("STATUS:", r.status_code)
    if r.status_code != 200:
        print(r.text[:300])

    r.raise_for_status()
    time.sleep(random.uniform(0.3, 1.2))  # анти-бан
    return r.json()
