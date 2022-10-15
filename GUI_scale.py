from tkinter import *


def submit():
    print("The temperature is " + str(scale.get()))


window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,  # orientation of scale
              font=("Consolas", 20),
              tickinterval=10,  #adds numeric indivators for value
              #showvalue=0, # hide current value
              resolution=5, #increment of slider
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111'
              )
scale.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()