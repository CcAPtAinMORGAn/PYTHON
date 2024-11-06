from tkinter import *

master = Tk()

# Set the size of the window
master.geometry("300x200")  # You can adjust this size as needed

# Create the Spinbox widget
w = Spinbox(master, from_=0, to=1000)

# Place the Spinbox widget in the center of the window
w.place(relx=0.5, rely=0.5, anchor=CENTER)

mainloop()

