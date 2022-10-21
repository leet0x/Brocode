print('''Exercise 4: Concatenate two lists in the following order''')

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concat_list = []
# Expected output:

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']


for l1 in list1:
    for l2 in list2:
        concat_list.append(l1 + l2)

print(concat_list)