# list comprehension = a way to create a new list with less syntax
#                     can mimic certain lambda functions, easier to read
#                     list = [expression for item in iterable]
#                     list = [expression for item in iterable if conditional]
#                     list = [expression if/else for item in iterable]

# classic way
squares = []
for i in range(1, 11):
    squares.append(i * i)

# using list comprehension
list = [i * i for i in range(1, 11)]
print(list)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
list = [i for i in students if i >= 60]
print(list)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
list = [i if i >= 60 else "FAILED" for i in students]
print(list)


