from tkinter import *

root = Tk()

text = Text(root)

text.insert(INSERT, "Hello.....")

text.insert(END, "Bye Bye.....")

text.pack()

text.tag_add("here", "1.1", "1.5")
#Created a tag "here" and selected a range from first letter to fifth letter

text.tag_add("start", "1.8", "1.13")

"""
Created a tag "start" and selected a range from eighth letter to
thirteenth letter
"""

text.tag_config("here", background="yellow", foreground="blue")

text.tag_config("start", background="blue", foreground="red")

root.mainloop()

