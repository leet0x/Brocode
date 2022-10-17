# nested loops = The "inner loop" wil finish all of  it's iterations before finishing one iteration of the "outer loop"

rows = int(input("How many rows? : "))
cols = int(input("How many columns?: "))
symbol = input("enter a symbol to use: ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end="")
    print(symbol)