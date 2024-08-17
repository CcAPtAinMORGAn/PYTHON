Num=int(input("Enter Number: "))

num1=0
num2=1
print(num1)
print(num2)

for i in range (0,Num-2):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3)
