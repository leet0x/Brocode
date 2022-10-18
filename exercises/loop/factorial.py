def factorial(num=0):
    fact = 1
    for i in range(num, 0, -1):
        fact *= i
    print(fact)


factorial(5)