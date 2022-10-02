from tkinter import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

space_background = PhotoImage(file="images/space_background.png")
background = canvas.create_image(0, 0, image=space_background, anchor=NW)


ufo_image = PhotoImage(file="images/ufo.png")
my_ufo_image = canvas.create_image(0, 0, image=ufo_image, anchor=NW)

width_ufo_image = ufo_image.width()
height_ufo_image = ufo_image.height()

while True:
    coordinates = canvas.coords(my_ufo_image)

    if coordinates[0] >= (WIDTH-width_ufo_image) or coordinates[0] < 0:
        xVelocity = -xVelocity

    if(coordinates[1] >= (HEIGHT-height_ufo_image) or coordinates[1] <0):
        yVelocity = -yVelocity

    canvas.move(my_ufo_image, xVelocity, yVelocity)

    window.update()
    time.sleep(0.01)


window.mainloop()
