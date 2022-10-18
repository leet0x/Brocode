# slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

name = "Lee Kschi"
first_name = name[0:3] # also name[:3]
last_name = name[4:]
funky_name = name[::2]
reversed_name = name[::-1]


print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)

print(website1[slice])
print(website2[slice])