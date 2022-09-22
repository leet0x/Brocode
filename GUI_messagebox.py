from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title="This is an info message box", message="You are happy!")
    # messagebox.showwarning(title="WARNING!", message="Showing some warning message here.")
    # messagebox.showerror(title="ERROR!!", message="Showing some error message here.")

    # if messagebox.askokcancel(title="ask ok cancel", message="Do you want  to do the  thing?"):
    #     print("You did  the thing.")
    # else:
    #     print("The thing was canceled.")

    # if messagebox.askretrycancel(title="ask retry cancel", message="Do you want  to retry the thing?"):
    #     print("you retried the thing")
    # else:
    #     print("You canceled the thing")

    # if messagebox.askyesno(title="ask yes no", message="Do you like cake?"):
    #     print("I like cake too.")
    # else:
    #     print("Why do you not like cake")

    # answer = messagebox.askquestion(title="ask question", message="Do you like pie?")
    # if answer == "yes":
    #     print("I like pie too.")
    # else:
    #     print("Why do you not like pie?")

    answer = messagebox.askyesnocancel(title="ask yes no cancel", message="Do you like to code?")
    if answer == True:
        print("you like to code")
    elif answer == False:
        print("Then why are you watching a video on coding?")
    else:
        print("You have dodged the question")


window = Tk()

button = Button(window, text="Click Me!", command=click)
button.pack()


window.mainloop()

