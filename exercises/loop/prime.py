def generatePrimeNumbers(start=0, end=0):
    prime_numbers = []
    for nr in range(start, end):
        if nr > 0:
            for i in range(2, nr):
                if nr % i == 0:
                    # not a prime number so break inner loop
                    break
                else:
                    if nr not in prime_numbers:
                        prime_numbers.append(nr)

    return prime_numbers


prime_number = generatePrimeNumbers(25, 50)
print(prime_number)
