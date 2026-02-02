from utils import clean, pick, format_date
import re

def parse_legal(item, api):
    guid = item.get("guid")
    if not guid:
        return None

    fed = api.fed_company(guid) or {}

    full_name = pick(fed.get("fullName"), item.get("name"))
    if full_name:
        # Пытаемся найти текст внутри кавычек «...» или "..."
        m = re.search(r'«(.+)»', full_name)
        if m:
            full_name = m.group(1)
        else:
            start = full_name.find('"')
            end = full_name.rfind('"')
            if start != -1 and end > start:
                full_name = full_name[start+1:end]

    return {
        "FullName": full_name,
        "INN": pick(fed.get("inn"), item.get("inn")),
        "OGRN": pick(fed.get("ogrn"), item.get("ogrn")),
        "KPP": clean(fed.get("kpp")),
        "RegistrationDate": format_date(fed.get("dateReg")),
        "Address": pick(fed.get("addressEgrul"), item.get("address")),
        "Region": clean(item.get("region")),
        "OKVED": clean((fed.get("okved") or {}).get("code")),
        "SourceURL": f"https://fedresurs.ru/companies/{guid}",
    }
