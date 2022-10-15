# from tkinter import *
# from tkinter import colorchooser
#
#
# def click():
#     color = colorchooser.askcolor() #assigns color to a variable
#     colorHex = color[1]  #assigns element at index 1 to a variable
#     window.config(bg=colorHex) #change background color
#
#
# window = Tk()
# window.geometry("420x420")
#
# button = Button(window, text="Click me", command=click)
# button.pack()
#
# window.mainloop()

###########################################
from tkinter import *
from tkinter import colorchooser

def click():
    color= colorchooser.askcolor()
    colorHex = color[1]
    label.config(fg=colorHex)

def backgroundChanger():
    color= colorchooser.askcolor()
    colorHex = color[1]
    label.config(bg=colorHex)

window = Tk()


window.geometry("800x500")
label = Label(window,text="This is some text",background='white',font=("Cascadia code",40),relief=RAISED,bd=10)
button = Button(window,text='Color Changer',command=click,background='white',font=("Cascadia code",12),relief=RAISED,bd=5)
button2 = Button(window,text='Background Changer',command=backgroundChanger,background='white',font=("Cascadia code",12),relief=RAISED,bd=5)
button.pack()
button2.pack()
label.pack()
window.mainloop()