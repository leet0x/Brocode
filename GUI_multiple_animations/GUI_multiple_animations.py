from tkinter import *
from Ball import *
import time

window = Tk()
window.title("GUI Multiple Balls animation")

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"white")

while True:
    volley_ball.move()
    window.update()
    time.sleep(0.01)



window.mainloop()