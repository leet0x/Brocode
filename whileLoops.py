#while loop = a statement that will execute a block of code until as long as its condition remains true

#one way of doing it
name = ""
while len(name) == 0:
    name = input("What is your name? : ")

print("Hello " + name)


#the other way of doing it

name = None
while not name:
    name = input("What is your name? : ")

print("Hello " + name)
