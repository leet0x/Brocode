# Exercise 6: Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Expected output:
# ["Mike", "Emma", "Kelly", "Brad"]

list2 = list(filter(lambda x: x != "", list1))

print(list2)