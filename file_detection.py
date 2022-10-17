import os

path = "test.txt"

if os.path.exists:
    print("That location exists")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is a folder")
else:
    print("That location doesnt exist")