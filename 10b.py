from tkinter import *

parent = Tk()
parent.title("Radiobutton")

radio1 = Radiobutton(parent, text='first', value=1)
radio2 = Radiobutton(parent, text='second', value=2)
radio3 = Radiobutton(parent, text='third', value=3)
radio1.grid(column=0, row=0)
radio2.grid(column=1, row=0)
radio3.grid(column=2, row=0)
parent.mainloop()