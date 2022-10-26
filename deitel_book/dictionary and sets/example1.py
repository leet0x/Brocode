country_codes = {"Finland": "fi",
                 "South Africa": "za",
                 "Nepal": "np"}
# country_codes.clear()

# determine whether it is empty or not
if country_codes:

    # iterate through a dictionary
    for key, value in country_codes.items():
        print(f"{key}: {value}")
else:
    print("is empty")

# updating a value
print(country_codes["Finland"])
print("Updating...")
country_codes["Finland"] = "fifi"
print(country_codes["Finland"])

# adding a new key-value pair
country_codes["Albania"] = "Al"
print(country_codes)

# removing a key value pair by using "del" key word
# del country_codes["Finland"]
# or with pop()
# country_codes.pop("Finland")
print(country_codes)

# use get() to prevent an error frm trying to access a key
# it does not exists. by using get it will return "None"
print(country_codes.get("Italy"))

# testing whether a dictionary contains a specified key
print("Albania" in country_codes) # True
print("Albania" not in country_codes) # False

# methods keys() and values() can be used to iterate through
# only a dictionary's keys or values respectively
print(country_codes.keys())
print(country_codes.values())

















