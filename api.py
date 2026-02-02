import time
import random
from curl_cffi import requests

BANKROT = "https://bankrot.fedresurs.ru/backend"
FED = "https://fedresurs.ru/backend"

class FedAPI:
    def __init__(self):
        self.bankrot = requests.Session(impersonate="chrome124")
        self.fed = requests.Session(impersonate="chrome124")

        self.bankrot.headers.update({
            "user-agent": "Mozilla/5.0 Chrome/124",
            "accept": "application/json, text/plain, */*",
            "referer": "https://bankrot.fedresurs.ru/bankrupts",
            "origin": "https://bankrot.fedresurs.ru",
        })

        self.fed.headers.update({
            "user-agent": "Mozilla/5.0 Chrome/124",
            "accept": "application/json, text/plain, */*",
            "referer": "https://fedresurs.ru/",
            "origin": "https://fedresurs.ru",
        })

        # warmup
        try:
            self.bankrot.get("https://bankrot.fedresurs.ru/bankrupts")
            time.sleep(2)
        except:
            pass

    def fetch(self, session, url):
        for _ in range(3):
            try:
                r = session.get(url, timeout=25)
                if r.status_code != 200:
                    print(f"[HTTP {r.status_code}] {url}")
                    time.sleep(random.uniform(1,2))
                    continue
                return r.json()
            except Exception as e:
                print("ERR", e)
                time.sleep(1)
        return {}

    # списки
    def list_legals(self, offset, limit=15):
        url = f"{BANKROT}/cmpbankrupts?limit={limit}&offset={offset}"
        return self.fetch(self.bankrot, url).get("pageData", [])

    def list_persons(self, offset, limit=15):
        url = f"{BANKROT}/prsnbankrupts?limit={limit}&offset={offset}"
        return self.fetch(self.bankrot, url).get("pageData", [])

    # детали
    def fed_company(self, guid):
        return self.fetch(self.fed, f"{FED}/companies/{guid}")

    def fed_person(self, guid):
        return self.fetch(self.fed, f"{FED}/persons/{guid}")
