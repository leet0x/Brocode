# Exercise 1: Convert two lists into a dictionary
# Below are the two lists. Write a Python program to convert them into a
# dictionary in a way that item from list1 is the key and item from list2
# is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# first solution
# dict = {}
#
# for keys, values in zip(keys, values):
#     dict.update({keys: values})
# print(dict)

# second solution
res_dict = dict(zip(keys, values))
print(res_dict)