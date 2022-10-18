from tkinter import *

count = 0
def click():
    global count
    count += 1
    print("button clicked")
    print(count)


window = Tk()
window.title("some button")

icon = PhotoImage(file="python logo.png")
window.iconphoto(True, icon)

button = Button(window,
                text="click me",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE, # disables the button
                image=icon,
                compound="bottom"
                )
button.pack()


window.mainloop()