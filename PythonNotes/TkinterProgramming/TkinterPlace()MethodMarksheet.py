from tkinter import *

def calculate_total():
    try:
        # Get values from Entry widgets, convert to float and sum
        physics = float(E1.get())
        maths = float(E2.get())
        total = physics + maths
        E3.delete(0, END)  # Clear the "Total" entry field
        E3.insert(0, str(total))  # Insert the result into the "Total" field
        percentage=(total/200)*100
        E4.delete(0, END)
        E4.insert(0, str(percentage))
        
    except ValueError:
        E3.delete(0, END)  # Clear the "Total" field in case of invalid input
        E3.insert(0, "Invalid input")

# Set up main window
top = Tk()

# Physics label and entry
L1 = Label(top, text="Physics")
L1.place(x=10, y=10)
E1 = Entry(top, bd=5)
E1.place(x=60, y=10)

# Maths label and entry
L2 = Label(top, text="Maths")
L2.place(x=10, y=50)
E2 = Entry(top, bd=5)
E2.place(x=60, y=50)

# Total label and entry
L3 = Label(top, text="Total")
L3.place(x=10, y=150)
E3 = Entry(top, bd=5)
E3.place(x=60, y=150)

# Percentage Calculation
L4 = Label(top, text="Percentage")
L4.place(x=10, y=190)
E4 = Entry(top, bd=5)
E4.place(x=80, y=190)

# Add button
B = Button(top, text="Add", command=calculate_total)
B.place(x=100, y=100)

# Window geometry
top.geometry("250x250+10+10")

# Start the GUI event loop
top.mainloop()
