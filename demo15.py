from tkinter import *

root = Tk()

label3 = Label(root, text="Happy new year ", bg="red",fg="white")
label3.config(font=("Raleway", 22))

label2 = Label(root, text="Happy Birthday Day !!", bg="red",fg="white")
label2.config(font=("Raleway",22))

label4 = Label(root, text="happy diwali", bg="red",fg="white")
label4.config(font=("Raleway", 22))



def greet():
    label2.pack()


def click():

    label3.pack()


def click2():


    label4.pack()


label = Label(root, text="Welcome, to the Greetings Application!!", bg="red",fg="white")
label.config(font=("Raleway", 22))
label.pack()

btn = Button(root, text="birthday CLICK ME", bg="lime", fg="black", width = 30, height=1, command=greet)
btn.config(font=("Raleway",22))
btn.pack()

btn2 = Button(root, text="new year CLICK ME ", bg="lime",fg="black", width = 30, height=1, command=click)
btn2.config(font=("Raleway", 22))
btn2.pack()


btn3= Button(root, text="diwali CLICK ME", bg="lime", fg="black", width = 30, height=1, command=click2)
btn3.config(font=("Raleway",22))
btn3.pack()


root.mainloop()
