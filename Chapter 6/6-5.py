rivers = {}
rivers["nile"]="egypt"
rivers["amazon"]="usa"
rivers["indus"]="pakistan"

for k,v in rivers.items():
    if v=="usa":
        print(f"The {k.title()} runs through the {v.upper()}.")
    else:
        print(f"The {k.title()} runs through the {v.title()}.")

#2nd method same output
rivers = {}
rivers["nile"]="egypt"
rivers["amazon"]="usa"
rivers["indus"]="pakistan"
for k,v in rivers.items():
    print(f"The {k.title()} runs through the {v.upper() if v=="usa" else v.title()}.")
for river in rivers.keys():
    print(f"Name : {river.title()}")
for country in rivers.values():
    print(f"Country : {country.upper() if country=="usa" else country.title()}")

# Chat gpt practice
countries = {
    "pakistan": "islamabad",
    "usa": "washington",
    "turkey": "ankara",
    "uk": "london"
}
for k,v in countries.items():
    print(f"The capital of {k.upper() if k=="usa" or k=="uk" else k.title()} is {v.title()}")