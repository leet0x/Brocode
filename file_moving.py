import os

source = "test1.txt"
destination = "execs\\test1.txt"

try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print("was not found")
