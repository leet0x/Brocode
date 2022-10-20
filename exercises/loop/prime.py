def generatePrimeNumbers(start=0, end=0):
    prime_numbers = []
    for nr in range(start, end):
        if nr > 1:
            for i in range(2, nr):
                if nr % i == 0:
                    break
                else:
                    if nr not in prime_numbers:
                        prime_numbers.append(nr)
    return prime_numbers


def reverse_list(prime_numbers):
    # prime_numbers.reverse()
    return prime_numbers[::-1]


def modify(prime_numbers):
    prime_numbers[:3] = ["one", "two", "three"]
    return prime_numbers


def delete(prime_numbers):
    del prime_numbers[:3]
    return prime_numbers


def sort_list(prime_numbers):
    prime_numbers.sort()
    # prime_numbers.sort(reverse=True)
    return prime_numbers


def extend_list(current_list=[], to_add_list = []):
    current_list.extend(to_add_list)
    return current_list


prime_number = generatePrimeNumbers(start=25, end=50)
print(prime_number)
print(reverse_list(prime_number))
print(modify(prime_number))
print(delete(prime_number))
# sort_list(prime_number)
print(sort_list(prime_number))
prime_number *=2
print(prime_number)
print(prime_number.index(33, 2))
to_add = ["red", "yellow", "orange"]
print(extend_list(prime_number, to_add))
to_add.remove("yellow")
print(to_add)
to_add.clear()
print(to_add)

#list comprehension
# so instead of writing a for loop for creating a list with some generated items
# we can just write the following
# list = [item for item in range(1, 6)]
# print(list)
# OR even shorter
list = list(range(1, 6))
print(list)

# filtering list comprehension with if clauses
filtered_list = [item for item in range(1, 6) if item % 2 == 0]

print(filtered_list)

# list comprehension that processes another list's elements
color = ["red", "orange", "blue", "white", "black"]
color2 = [item.upper() for item in color]
print(color2)


names = ["Bob", "Sue", "Amanda"]
grade_point_averages = [3.5, 4.0, 3.75]
# zipped = zip(names, grade_point_averages)
for name, gpa in zip(names, grade_point_averages):
    print(f"{name}: {gpa}")

# Two dimensional lists
grades = [[77, 68, 86, 73],
          [96, 87, 89, 81],
          [70, 90, 86, 81]]
for row in grades:
    # print(row)
    for item in row:
        print(item, end=" ")
    print()

