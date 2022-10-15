# text widget = functions like a text area, you can enter multiple lines of text
from tkinter import *


def click():
    input = text.get("1.0", END)
    print(input)


window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 25),
            height=8, #nr of rows
            width=20, #nr of characters
            padx=20,
            pady=20,
            fg="purple")
text.pack()

button = Button(window, text="submit", command=click)
button.pack()
window.mainloop()

