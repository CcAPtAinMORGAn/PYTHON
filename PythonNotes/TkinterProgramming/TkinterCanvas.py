from tkinter import *
from tkinter import messagebox
top = Tk()
C = Canvas(top, bg="blue", height=250, width=300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
line = C.create_line(100,100,200,200,fill='white')
C.pack()
top.mainloop()

"""
The tuple has four numbers: (x1, y1, x2, y2).

x1 = 10: The x-coordinate of the top-left corner of the bounding box.
y1 = 50: The y-coordinate of the top-left corner of the bounding box.
x2 = 240: The x-coordinate of the bottom-right corner of the bounding box.
y2 = 210: The y-coordinate of the bottom-right corner of the bounding box.
"""

"""
(10, 50) ┌───────────────────────────────────────────────┐
         │                                           │
         │                                           │
         │                                           │
         │                                           │
         └───────────────────────────────────────────────┘
                              (240, 210)
"""
