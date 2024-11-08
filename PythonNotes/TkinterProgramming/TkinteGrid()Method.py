from tkinter import *
root = Tk( )
b=0
for r in range(6):
## r loop will go like 0,1,2,3,4,5    
     for c in range(6):
     ## c loop will go like 0,1,2,3,4,5
         b+=1
         Button(root, text=str(b),
             borderwidth=1 ).grid(row=r,column=c)
root.mainloop()


##
##b=0
##for i in range(6):
##    for j in range(6):
##        b+=1
##        print(b)
