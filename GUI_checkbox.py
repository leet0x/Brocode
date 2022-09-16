from tkinter import *


def display():
    if x.get():
        print("You agreed")
    else:
        print("You disagreed")


window = Tk()

photo_image = PhotoImage(file="images/python_logo.png")


x = BooleanVar()
checkbox_button = Checkbutton(window,
                              text="I agree to something",
                              variable=x,
                              font=("Arial", 20),
                              fg="#00FF00",
                              bg="Black",
                              activeforeground="#00FF00",
                              activebackground="Black",
                              command=display,
                              onvalue=True,
                              offvalue=False,
                              image=photo_image,
                              compound="left",
                              padx=25,
                              pady=10)
checkbox_button.pack()

window.mainloop()
