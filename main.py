from api import FedAPI
from parser_legals import parse_legal
from parser_persons import parse_person
from excel_writer import ExcelWriter
import time

api = FedAPI()
writer = ExcelWriter("bankrot.xlsx")

# ---- LEGALS ----
legals = []
offset = 0
quantity = 500
while len(legals) < quantity:
    for item in api.list_legals(offset):
        row = parse_legal(item, api)
        if row:
            legals.append(row)
            print("LEGAL", row["FullName"])
        if len(legals) >= quantity:
            break
    offset += 15
    time.sleep(1)

writer.write("legal", legals)

# ---- PERSONS ----
persons = []
offset = 0

while len(persons) < quantity:
    for item in api.list_persons(offset):
        row = parse_person(item, api)
        if row:
            persons.append(row)
            print("PERSON", row["FullName"])
        if len(persons) >= quantity:
            break
    offset += 15
    time.sleep(1)

writer.write("person", persons)

print("DONE")
