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

# converting dictionary Keys, Values and key-value pairs t Lists
keys_list = list(country_codes.keys())
print(keys_list)
values_list = list(country_codes.values())
print(values_list)
key_value_list = list(country_codes.items())
print(key_value_list)

# processing keys in sorted order
for keys in sorted(country_codes.keys()):
    print(keys, end=" ")
print()
# dictionary comparisons
# the comparison operator == and != can be  used to determine whether
# two dictionaries have identical or different contents.
# An equals (==) comparison evaluates to True if  both dictionaries
# have the same key-value pairs, regardless of the order in which
# those key-value pairs were added to each dictionary

country_capitals1 = {"Belgium": "Brussels",
                     "Haiti": "Port-au-Prince"}
country_capitals2 = {"Nepal": "Kathmandu",
                     "Uruguay": "Montevideo"}
country_capitals3 = {"Haiti": "Port-au-Prince",
                     "Belgium": "Brussels"}
print(country_capitals1 == country_capitals2) # False
print(country_capitals1 == country_capitals3) # True
print(country_capitals1 != country_capitals2) # True