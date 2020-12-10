from tkinter import *

root = Tk()

label = Label(root, text="Do you like Icecream", fg="black")
label.config(font=('Arial',22))

btn = Button(text="YES", bg="black", fg="Yellow")
btn.config(font=('Arial',12))
btn.grid(row=2, column=2)

btn_2 = Button(text="NO", bg="black", fg="lime")
btn_2.config(font=("Arial",12))
btn_2.grid(row=2, column=3)



root.mainloop()

