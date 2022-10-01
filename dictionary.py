# dictionary = a changeable, unordered collection of unique key:value pairs.
#             Fast because they use hashing, allow us to access a value quickly

capitals = {"USA": "Washington DC",
            "India": "New Dehli",
            "China": "Beijing",
            "Russia": "Moscow"}

capitals.update({"Germany": "Berlin"})
print(capitals.get("USA"))
print(capitals.items())
print(capitals.keys())
print(capitals.values())

for key, value in capitals.items():
    print(value)