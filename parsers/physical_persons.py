from client import get_bankrot, get_fed

def list_persons(limit=50, offset=0):
    return get_bankrot("/prsnbankrupts", {
        "limit": limit,
        "offset": offset,
        "isActiveLegalCase": None
    }).get("pageData", [])

def person_details(guid):
    return get_fed(f"/persons/{guid}")

def map_person(base, d):
    case = base.get("lastLegalCase", {}) or {}
    status = case.get("status", {}) or {}

    return {
        "FullName": base.get("fio"),
        "INN": base.get("inn"),
        "SNILS": base.get("snils"),
        "BirthDate": d.get("birthDate"),
        "Address": d.get("address"),
        "Region": d.get("region"),
        "Status": status.get("description"),
        "CaseNumber": case.get("number"),
        "Manager": case.get("arbitrManagerFio"),
        "SourceURL": f"https://bankrot.fedresurs.ru/PersonCard/{base.get('guid')}"
    }
