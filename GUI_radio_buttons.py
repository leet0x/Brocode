from tkinter import *


def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered hamburger!")
    elif x.get() == 2:
        print("You ordered hotdog!")
    else:
        print("huh?")


window = Tk()

food = ["pizza", "hamburger", "hotdog"]

pizza_image = PhotoImage(file="images/pizza.png")
hamburger_image = PhotoImage(file="images/hamburger.png")
hotdog_image = PhotoImage(file="images/hotdog.png")

food_images = [pizza_image, hamburger_image, hotdog_image]

x = IntVar()
for i in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[i],  # adds text to radio buttons
                               variable=x,  # groups radio buttons together if they share the same variable
                               value=i,  # assigns each radiobutton a different value
                               padx=25,  # adds padding on x-axis
                               font=("Impact", 50),
                               image=food_images[i],  # adds image to radiobutton
                               compound="left",  # adds image & text (left side)
                               # indicatoron=0, # eliminate circle indicators
                               # width = 375, # sets width of radio buttons
                               command=order  # set command of radiobutton to function
                               )
    radio_button.pack(anchor=W)
window.mainloop()
