from tkinter import *

root = Tk()

l2 = Label(root, text="username:")
l2.config(font=("Arial", 14))

l3 = Label(root, text="password:")
l3.config(font=("Arial", 14))

username = StringVar()
password = StringVar()

e1 = Entry(root, textvariable=username)
e2 = Entry(root, textvariable=password, show="*")


l2.grid(row=0, column=0)
e1.grid(row=0, column=1)

l3.grid(row=1, column=0)
e2.grid(row=1, column=1)

def greet():
    username_show = f"Your username is: {username.get()}"

    label_2 = Label(root, text="Welcome to Q and A")
    label_2.config(font=("Arial",15))
    label_2.pack()

btn_1 = Button(root, text="SUBMIT", bg="orange", fg="yellow", command=greet)
btn_1.config(font=("Arial",12))
btn_1.pack()


def click_1 ():
    label_4 = Label(root,text="yes it's right")
    label_4.config(font=("Arial",22))
    label_4.pack()

def click_2():
    label_5 = Label(root, text="no it's wrong")
    label_5.config(font=("Arial", 22))
    label_5.pack()


def QA_1():

    label_3 = Label(root, text="who was the first women prime minister of india??")
    label_3.config(font=("Arial", 15))
    label_3.pack()

    btn_2 = Button(root, text="Indira Gandhi", command=click_1)
    btn_2.pack()

    btn_3 = Button(root, text="shah Jahan", command=click_2)
    btn_3.pack()

    btn_4 = Button(root, text="Fathima Beevi", command=click_2)
    btn_4.pack()

def QA_2():
    label_4 = Label(root, text="who built the red Fort in Delhi??")
    label_4.config(font=("Arial", 15))
    label_4.pack()

    btn_5 = Button(root, text="Indira Gandhi", command=click_2)
    btn_5.pack()

    btn_6 = Button(root, text="shah Jahan", command=click_1)
    btn_6.pack()

    btn_7= Button(root, text="Fathima Beevi", command=click_2)
    btn_7.pack()
def QA_3():
    label_4 = Label(root, text="what is the highest dam in india??")
    label_4.config(font=("Arial", 15))
    label_4.pack()

    btn_5 = Button(root, text="Tehre Dam", command=click_2)
    btn_5.pack()

    btn_6 = Button(root, text="Srisilam Dam", command=click_1)
    btn_6.pack()

    btn_7= Button(root, text="Hirakud Dam", command=click_2)
    btn_7.pack()

btn_8 = Button(root, text="Start Question 1", command=QA_1)
btn_8.config(font=("Arial",12))
btn_8.pack()

btn_9 = Button(root, text="Start Question 2", command=QA_2)
btn_9.config(font=("Arial",12))
btn_9.pack()

btn_10 = Button(root,text="start Question 3",command=QA_3)
btn_10.config(font=("Arial",12))
btn_10.pack()
root.mainloop()



