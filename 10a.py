from tkinter import *

parent = Tk()
mytext = Text(parent)
mytext.insert('1.0', 'i like python')
mytext.insert('1.2', "don't ")
mytext.delete('1.0')
mytext.delete('end-1 chars')

mytext.pack()
parent.mainloop()
