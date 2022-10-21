# Exercise 5: Iterate both lists simultaneously

# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
#
# Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# Expected output:
#
# 10 400
# 20 300
# 30 200
# 40 100

for l1 in zip(list1, list2[::-1]):
    print(l1[0], l1[1])

