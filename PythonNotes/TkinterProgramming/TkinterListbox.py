from tkinter import *

import tkinter

x = Tk()

#----------Listbox(x)
Lb1 = Listbox(x)

Lb1.insert(1, "Python")

Lb1.insert(2, "Perl")

Lb1.insert(3, "C")

Lb1.insert(4, "PHP")

Lb1.insert(5, "JSP")

Lb1.insert(6, "Ruby")

Lb1.pack()

#--------x.mainloop
x.mainloop()

