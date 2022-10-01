# index operator = gives access to a sequences element (str, list, tuple)

name = "Lee Kschi."

if(name[0].isupper()):
    name = name.lower()
first_name = name[:3]
last_name = name[4:]
last_character = name[-1]

print(name)
print(first_name)
print(last_name)
print(last_character)