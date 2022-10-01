#canvas = widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)

canvas.create_line(0, 0,   500, 500, width=5, fill="blue")
canvas.create_line(0, 500, 500, 0,   width=5, fill="red")
canvas.create_arc( 0, 0,   500, 500, width=5, fill="pink")
canvas.create_rectangle(500/2, 500/2, 0, 0, width=5, fill="black")

canvas.pack()


window.mainloop()