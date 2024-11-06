from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("100x100")
def helloCallBack():
 msg=messagebox.showinfo( "Hello Python", "Hello world")
B = Button(top, text ="Press For Hello World", command = helloCallBack)
B.place(x=50,y=50)
"""
B.place(x=500,y=500)
B.place(x=1,y=1)

"""
top.mainloop()

