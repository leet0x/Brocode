# Exercise 5: Create a dictionary by extracting the keys
# from a given dictionary
# Write a Python program to create a new dictionary by extracting
# the mentioned keys from the below dictionary.
# Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

# Expected output:
# {'name': 'Kelly', 'salary': 8000}

res_dict = {}

for keys1, values in sample_dict.items():
    if keys1 in keys:
        res_dict.update({keys1: values})
    # print(keys1, values)
print(res_dict)