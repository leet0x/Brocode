from tkinter import *


def openFile():
    print("you opened some file")


def saveFile():
    print("You saved some file")


def copy():
    print("You copied some text!")


def cut():
    print("You cut some text!")


def paste():
    print("You pasted some text!")


def appearance():
    print("You changed the appearance!")


def compare():
    print("You compared something!")


window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Paste", command=paste)

viewMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=viewMenu)
viewMenu.add_command(label="Appearance", command=appearance)
viewMenu.add_command(label="Compare", command=compare)

window.mainloop()
