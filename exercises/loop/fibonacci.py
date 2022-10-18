def fib():
    fib_seq = [0, 1]
    for i in range(0, 50):
        fib_seq.append(fib_seq[i+1] + fib_seq[i])

    print(fib_seq)
fib()