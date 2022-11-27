# Exercise 2: Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# first solution
# dict1.update(dict2)
# res_dict = dict1
# print(res_dict)

# second solution
# you can merge two dictionaries by using two preceding asterisks "**"
# res_dict = {**dict1, **dict2}
res_dict = {**dict1}
print(res_dict)