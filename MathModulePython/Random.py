import random
ynum=int(input("enter number between 1 to 10:"))
lucky=random.choice(range(1,11))
print("Lucky Number:",lucky)
if(ynum==lucky):
    print("WINNER")
else:
    print("Better Luck Next Time")
