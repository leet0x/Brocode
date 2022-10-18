def sum_curr_plus_prev(times):
    for i in range(times):
        if i > 0:
            sum = i + (i - 1)
            print(f'current number:{i} previous number {i - 1} sum: {sum}')
        else:
            sum = i + i
            print(f'current number:{i} previous number {i} sum: {sum}')




sum_curr_plus_prev(10)