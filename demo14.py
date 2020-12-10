from tkinter import *

root = Tk()
label = Label(root, text="Do you have salt in your toothpaste?")
label.config(font=("Arial",22))

label_2 = Label(root, text="It's good that you have salt!!", fg="green", bg="yellow")
label_2.config(font=("Arial", 18))

label_3 = Label(root, text="what?? you'd don't seltin your too toothpaste, tye the new COLGATE!!!!", fg="red",
                bg="black")
label_3.config(font=("Arial", 18))
text_widget = Entry(root, textvariable=StringVar(), font=("Arial", 22))


def click():
    label_2.pack()

def close():
    label_3.pack()


btn1 = Button(root, text="Yes", width="22", bg="yellow", fg="green", command=click)
btn1.config(font=("Arial",22))
btn2 = Button(root, text="No", width="22",bg="red",fg="white", command=close)
btn2.config(font=("Arial",22))

label.pack()
btn1.pack()
btn2.pack()

root.mainloop()

