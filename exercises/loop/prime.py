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


def reverse(prime_numbers):
    return prime_numbers[::-1]


def modify(prime_numbers):
    prime_numbers[:3] = ["one", "two", "three"]
    return prime_numbers


def


prime_number = generatePrimeNumbers(start=25, end=50)
print(prime_number)
print(reverse(prime_number))
print(modify(prime_number))


