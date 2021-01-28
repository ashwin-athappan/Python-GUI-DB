from tkinter import *

parent = Tk()
label1 = Label(parent, text='a list of favourite languages...')
listbox = Listbox(parent)
listbox.insert(1, 'PHP')
listbox.insert(2, 'python')
listbox.insert(3, 'C')
listbox.insert(4, 'C++')
label1.pack()
listbox.pack()
parent.mainloop()
