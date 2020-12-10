from tkinter import *

root = Tk()


l2 = Label(root, text="enter a number:")
l2.config(font=("Arial", 14))
l2.pack()

number = IntVar()

e1 = Entry(root, textvariable= number)


login_button = Button(root, text="SUBMIT")
login_button.config(font=("Arial", 12))


text_widget = Entry(root, textvariable=IntVar(), font=("Arial",14))
name = text_widget.get()
text_widget.pack()

login_button.pack()
root.mainloop()

