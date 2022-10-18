# John Hunt
# A Beginners
# Guide to Python 3
# Programming

const = 0.6214
distKm = input("enter your input in km: ")
if distKm.isnumeric():
    distKm = int(distKm)
    if distKm < 0:
        distKm = int(input("Negative numbers cannot be entered: "))
    else:
        distMiles = distKm / const
else:
    distKm = int(input("only numeric :"))

print(str(distKm) + " Km is equal to " + str(distMiles) + " Miles")