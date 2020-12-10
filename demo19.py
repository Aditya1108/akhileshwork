from tkinter import *

root = Tk()
text_widget = Entry(root, textvariable=StringVar(), font=("Arial",14))
name = text_widget.get()


def greet():
    name = text_widget.get()

    label = Label(root, text=name)
    label.config(font=("Arial", 14))
    label.pack()

btn = Button(root, text="SUBMIT", bg="orange", fg="yellow", command=greet)
btn.config(font=("Airal",12))
text_widget.pack()
btn.pack()


root.mainloop()
