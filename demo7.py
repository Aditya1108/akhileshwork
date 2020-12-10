from tkinter import *

root = Tk()
root.title("Scrollbar - Example")
root.geometry("800x2000")


scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)
scrollbar.config(command = root)

root.mainloop()
