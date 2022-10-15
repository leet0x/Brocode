from tkinter import *
from tkinter import filedialog


def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Alba 3\\Pictures",
                                          title="Open file okay?",
                                          filetypes=(("Text files only", "*.txt"),
                                                     ("All files", "*.*")))
    file = open(filepath, "r")
    print(file.read())
    file.close()


window = Tk()

button = Button(window, text="Open", command=openFile)
button.pack()

window.mainloop()