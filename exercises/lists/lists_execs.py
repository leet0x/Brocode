# reverse a list in python

def generate_numbers(start=0, end=0, steps=0):
    list = []
    for nr in range(start, end, steps):
        list.append(nr)
    return list


def reverse_exec(generated_list):
    generated_list.reverse() # first method
    reversed_list = generated_list
    # reversed_list = generated_list[::-1]  # second method
    return reversed_list



reversed = reverse_exec(generate_numbers(100, 600, 100))
print(reversed)
print()

print('''# Exercise 2: Concatenate two lists index-wise''')

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
concat_list = [i + j for i, j in zip(list1, list2)]
print(concat_list)
print()

# Exercise 3: Turn every item of a list into its square
print('''# Exercise 3: Turn every item of a list into its square''')
numbers = generate_numbers(1, 11, 1)
print(numbers)

numbers_squared = [i** 2 for i in numbers]
print(numbers_squared)
print()














