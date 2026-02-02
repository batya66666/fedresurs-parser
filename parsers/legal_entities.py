from client import get_bankrot, get_fed

def list_companies(limit=50, offset=0):
    data = get_bankrot("/cmpbankrupts", {
        "limit": limit,
        "offset": offset,
        "isActiveLegalCase": None
    })
    return data.get("pageData", [])

def company_details(guid):
    return get_fed(f"/companies/{guid}")

def map_company(base, d):
    case = base.get("lastLegalCase", {}) or {}
    status = case.get("status", {}) or {}

    return {
        "FullName": base.get("name"),
        "INN": base.get("inn"),
        "OGRN": base.get("ogrn"),
        "KPP": base.get("kpp"),
        "AuthorizedCapital": d.get("authorizedCapital"),
        "RegistrationDate": d.get("regDate"),
        "Address": d.get("address"),
        "Region": d.get("region"),
        "LegalForm": d.get("legalForm"),
        "OKVED": d.get("okved"),
        "Status": status.get("description"),
        "ProcedureType": case.get("procedureType"),
        "CaseNumber": case.get("number"),
        "CaseStatus": case.get("caseStatus"),
        "CaseEndDate": case.get("endDate"),
        "ArbitrationManagerName": case.get("arbitrManagerFio"),
        "ArbitrationManagerINN": case.get("arbitrManagerInn"),
        "ManagerAppointmentDate": case.get("managerAppointmentDate"),
        "PublicationsCount": d.get("publicationsCount"),
        "TradesCount": d.get("tradesCount"),
        "SourceURL": f"https://bankrot.fedresurs.ru/CompanyCard/{base.get('guid')}"
    }
