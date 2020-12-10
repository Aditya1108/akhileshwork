from tkinter import *

root = Tk()
text_widget = Entry(root, textvariable=StringVar(), font=("Arial", 100))
text_widget.pack()

label = Label(root, text=f"Hello,{text_widget}")
label.config(font=("Arial", 22))


def greet():
    label.pack()


btn = Button(root, text="SUBMIT", bg="orange", fg="yellow", command=greet)

root.mainloop()



