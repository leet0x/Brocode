from tkinter import *


def submit():
    food = []

    for i in listbox.curselection():
        food.insert(i, listbox.get(i))

    for i in food:
        print(i)
    # print(listbox.get(listbox.curselection()))


def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())


def delete():
    # listbox.delete(listbox.curselection())
    # listbox.config(height=listbox.size())

    for i in reversed(listbox.curselection()):
        listbox.delete(i)

    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  selectmode=MULTIPLE)
listbox.pack()

food_list = ["pizza", "pasta", "garlic bread", "soup", "salad"]

index = 0
for item in food_list:
    listbox.insert(index, item)
    index = index + 1


# listbox.insert(0, "pizza")
# listbox.insert(1, "pasta")
# listbox.insert(2, "garlic bread")
# listbox.insert(3, "soup")
# listbox.insert(4, "salad")

listbox.config(height=listbox.size())

entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window,
                       text="Submit",
                       command=submit)
submit_button.pack(side=LEFT)

add_button = Button(window,
                    text="Add",
                    command=add)
add_button.pack(side=LEFT)

delete_button = Button(window,
                       text="Delete",
                       command=delete)
delete_button.pack(side=LEFT)

window.mainloop()

