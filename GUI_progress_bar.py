from tkinter import *
from tkinter.ttk import *
import time


def start():
    # tasks = 10 #nr of tasks
    # x = 0 #the current task that we're on

    GB = 100 #nr of tasks
    download = 0 #the current task that we're on
    speed = 1

    while download < GB:
        time.sleep(0.05)
        bar["value"] += speed
        download += 1
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB))
        window.update_idletasks()


window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack()

percentLabel = Label(window, textvariable=percent)
percentLabel.pack()

textLabel = Label(window, textvariable=text)
textLabel.pack()

button = Button(window, text="Download", command=start)
button.pack()


window.mainloop()

