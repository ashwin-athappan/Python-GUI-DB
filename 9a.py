from tkinter import *

r = Tk()
b = Button(r, text='click_me', command=r.destroy)
b.pack()
r.mainloop()
