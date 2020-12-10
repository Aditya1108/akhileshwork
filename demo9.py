from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Combobox!!")
root.geometry('500x200')

n = StringVar()
combobox = ttk.Combobox(root, width=27, textvariable = n)
combobox.pack()









root.mainloop()
