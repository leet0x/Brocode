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