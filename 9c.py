from tkinter import *

root = Tk()
my_boolean_var = BooleanVar()
my_checkbutton = Checkbutton(root, text="check when the option is true", variable=my_boolean_var)
my_checkbutton.pack()
root.mainloop()
