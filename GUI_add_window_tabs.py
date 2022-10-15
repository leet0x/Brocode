from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both") # expand = to use any space not otherwise used
                                        # fill = fill space on x and y axes

Label(tab1, text="Hello, this is tab 1", height=50, width=50).pack()
Label(tab2, text="Good bye, this is tab 2", height=50, width=50).pack()

window.mainloop()

