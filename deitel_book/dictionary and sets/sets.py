# creating a set with the built-in set functin from another collection
# of values.
numbers = list(range(10)) + list(range(5))
print(numbers)
numbers_set = set(numbers)
print(numbers_set)

# creating an empty set
empty_set = set()

'''mathematical set operations'''
# union
set1 = {1, 3, 5}
set2 = {2, 3, 4}
print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"union between set1 and set2: {set1 | set2}")
print(set1.union([20, 20, 3, 40, 40]))

#intersection
print(f"intersection between set1 and set2: {set1 & set2}")

# difference
print(f"difference between set1 and set2: {set1 - set2}")

# symmetric difference
print(f"symmetric difference between set1 and set2: {set1 ^ set2}")

# two sets a disjoint when they do not have any common elements
print(set1.isdisjoint(set2))

# add elements
set1.add(8)
print(set1)

# remove elements
set1.remove(1)
print(set1)

# method discard() also removes its argument from the set but does not
# cause an exception if the value is not in the set.
# set1.discard(10)
set1.pop()
set1.clear() # empties the set

# set comprehension
