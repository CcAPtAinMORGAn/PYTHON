"""
q=int(input("Enter Qualification after 10th std"))
if(q==12):
    per=float(input("Enter Percentage "))
    if(per>=75):
        print("Admission granted ")
    else:
        print("Low Percentage ")
else:
    print("Not Qualified")
"""

Age=int(input("Enter Age Between 25-30: "))

if(Age>=25 and Age<30):

    Salary=float(input("Enter Salary: "))

    if(Salary>50000):
        print("Elligible For Marriage")
    else:
        print("Low Salary")
        
else:
    print("Not Elligible For Marriage")