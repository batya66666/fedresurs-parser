from utils import clean, pick, format_date

def parse_person(item, api):
    guid = item.get("guid")
    if not guid:
        return None

    fed = api.fed_person(guid) or {}

    return {
        "FullName": pick(item.get("fio"), fed.get("fullName")),
        "INN": pick(item.get("inn"), fed.get("inn")),
        "SNILS": pick(item.get("snils"), fed.get("snils")),
        "BirthDate": format_date(fed.get("birthdateBankruptcy")),
        "Address": pick(fed.get("address"), item.get("address")),
        "Region": clean(item.get("region")),
        "SourceURL": f"https://fedresurs.ru/persons/{guid}",
    }
