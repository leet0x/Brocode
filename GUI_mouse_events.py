from tkinter import *


def doSomething(event):
    print("You did a thing on the coordinates: " + str(event.x) + ", " + str(event.y))


window = Tk()

# window.bind("<Button-1>", doSomething) #left mouse click
# window.bind("<Button-2>", doSomething) #scroll wheel button click
# window.bind("<Button-3>", doSomething) #right mouse click
# window.bind("<ButtonRelease>", doSomething) #left mouse button release
# window.bind("<Enter>", doSomething) #enter the window
# window.bind("<Leave>", doSomething) #Leaves the window
# window.bind("<Motion>", doSomething) #where the mouse moved

window.mainloop()

