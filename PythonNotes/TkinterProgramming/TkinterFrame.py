from tkinter import *

root = Tk()

frame = Frame(root)

frame.pack()



#------------------------------------------------------

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT )

#------------------------------------------------------

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

#------------------------------------------------------

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

#------------------------------------------------------

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

"""
bottomframe = Frame(root) creates a new frame inside the main window.

bottomframe.pack(side=BOTTOM) places the bottomframe at the bottom of the root window,
so any widgets added to this frame will appear near the bottom of the window.
"""

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()
    
