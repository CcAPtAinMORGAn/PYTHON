"""
amt=float(input("Enter Amount"))
if(amt>=25000):
    dis=amt*10/100
    print("Discount:",dis)
    print("Paid Amount",(amt-dis))

elif(amt>=20000 and amt<25000):
    dis=amt*7/100
    print("Discount:",dis)
    print("Paid Amount",(amt-dis))

elif(amt>=15000 and amt<20000):
    dis=amt*5/100
    print("Discount:",dis)
    print("Paid Amount",(amt-dis))

elif(amt>=10000 and amt<15000):
    dis=amt*3/100
    print("Discount:",dis)
    print("Paid Amount",(amt-dis))

else:
    print("No Discount")
    print("Paid Amount :",amt)
"""

Marks=float(input("Enter Marks out of 300"))
per=(Marks/300)*100
if(per>=75):
    print("Grade is A","and Percentage is",per,"%")

elif(per>=65 and per<75):
    print("Grade is B","and Percentage is",per,"%")

elif(per>=55 and per<65):
    print("Grade is C","and Percentage is",per,"%")

elif(per>=45 and per<55):
    print("Grade is D","and Percentage is",per,"%")

else:
    print("E Grade : Disqualified")

