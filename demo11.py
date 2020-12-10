import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ROBLOX")
root.geometry("500x200")

title = tk.Label(root,text="SIGN UP AND START HAVING FUN!!", bg="red")
title.config(font=("Arial Black",22))
title.grid(row=0,column=0,pady=5)

user_label = tk.Label(root,text="username: ")
user_label.config(font=("Calibri",22))
user_label.grid(row=1,column=1,pady=2)


pass_label = tk.Label(root,text="password: ")
pass_label.config(font=("Calibri",22))
pass_label.grid(row=2,column=1,pady=2)

entry1 = tk.Entry(root)
entry1.grid(row=1,column=2)

entry2 = tk.Entry(root,show="*")
entry2.grid(row=2,column=2)
root.mainloop()
