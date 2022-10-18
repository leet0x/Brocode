# import os
import shutil

# path = "test.txt"
path = "folder"

try:
    # os.remove(path)   #delete a file
    # os.rmdir(path)    #delet a folder
    shutil.rmtree(path)
except FileNotFoundError as e:
    print("was not found")
else:
    print("was deleted")


