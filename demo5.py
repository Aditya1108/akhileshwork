from tkinter import *

root = Tk()

def submit():
    password_show = f"Your password is: {password.get()}"
    username_show = f"Your username is: {username.get()}"

    label_password = Label(text=password_show)
    label_password.config(font=("Arial", 15))

    label_username = Label(text=username_show)
    label_username.config(font=("Arial", 15))

    label_username.grid(row=5, column=0)
    label_password.grid(row=6, column=0)


l2 = Label(root, text="username:")
l2.config(font=("Arial", 14))

l3 = Label(root, text="password:")
l3.config(font=("Arial", 14))

username = StringVar()
password = StringVar()

e1 = Entry(root, textvariable=username)
e2 = Entry(root, textvariable=password, show="*")

login_button = Button(root, text="Login", command=submit)
login_button.config(font=("Arial", 12))

l2.grid(row=0, column=0)
e1.grid(row=0, column=1)

l3.grid(row=1, column=0)
e2.grid(row=1, column=1)

login_button.grid(row=4, column=0)

root.mainloop()
