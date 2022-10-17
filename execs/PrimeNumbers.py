user_input = int(input("enter a number: "))


for i in range(1, user_input +1):
    for j in range(1, user_input+1):
        if i % j == 0:
            print("i: " + str(i) + " j: " + str(j))
