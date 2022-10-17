# sort() method = used with lists
# sort() function = used with iterable (tuples for example)

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"] #list
# students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs") #tuple

# sorting lists
students.sort(reverse=True)

for i in students:
    print(i)

# sorting tuples
# sorted_students = sorted(students, reverse=True)

# for i in sorted_students:
#     print(i)

#################################################

# When we have a list of tuples
# When we have a tuple of tuples
students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78))

student = lambda student: student[2]

# list of tuples
# students.sort(key=student, reverse=True)

# tuple of tuples (iterables)
sorted_students = sorted(students)

for i in students:
    print(i)

