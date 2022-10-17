from tkinter import *


def doSomething(event):
    label.config(text=event.keysym)


window = Tk()

#some comment
window.bind("<Key>", doSomething)

label = Label(window, font=("Helvetica", 50))
label.pack()

window.mainloop()