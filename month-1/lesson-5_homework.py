data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designations = []
codes = []
real_designations = ["O!", "Megacom", "Beeline"]
additional_O = {"0500", "0501", "0504", "0700"}
additional_Mega = {"0550", "0551", "0552", "0553"}
additional_Beeline = {"0501", "0505", "0507", "0509"}

for val in data:
    if val[0] == "0":
        codes.append(val)
    else:
        designations.append(val)

operators = dict(zip(designations, codes))

for key in operators.copy():
    if key in real_designations:
        print(f"компания {key} существует")
    else:
        print(f"компании {key} не существует. ({key} удален)")
        del operators[key]

operators["O!"] = additional_O
operators["Beeline"] = additional_Beeline
operators["Megacom"] = additional_Mega

for key, vallue in operators.items():
    print(f"{key} - {vallue}")