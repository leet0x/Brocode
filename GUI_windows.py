# Python tkinter GUI
from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Bro Code GUI program")

window.config(background="black") # you can also use hex

icon = PhotoImage(file="python logo.png")
window.iconphoto(True, icon)

window.mainloop() #place window on computer screen, listen for events