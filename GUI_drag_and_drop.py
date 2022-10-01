from tkinter import *

window = Tk()


label = Label(window, bg="red", width=10, height=5)
label.place(x=0, y=0)

label2 = Label(window, bg="yellow", width=10, height=5)
label2.place(x=100, y=100)

window.mainloop()