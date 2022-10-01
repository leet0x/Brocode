
# label = an area widget that hold text and/or an image within a window

from tkinter import *

window = Tk()

photo = PhotoImage(file="python logo.png")

label = Label(window,
              text="Hi",
              font=("Arial", 40, "bold"),
              fg="#00FF00",
              bg="black",
              relief=RIDGE,
              bd=10,
              padx=200,
              pady=100,
              image=photo,
              compound="bottom")
# label.pack()
label.place(x=0, y=100)

window.mainloop()