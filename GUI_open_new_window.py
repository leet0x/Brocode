from tkinter import *

def create_window():
    # on_top = Toplevel() #Toplevel() = new window on top of other windows, linked to a bottom window
    separate_window = Tk() #Tk() = new independent window
    window.destroy()



window = Tk()

Button(window, text="Create new window", command=create_window).pack()

window.mainloop()