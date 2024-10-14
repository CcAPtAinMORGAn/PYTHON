
Num=int(input("Enter Number: "))

reverse=0
copy=Num

while(copy>0):
    digit=copy%10
    copy=copy//10
    reverse=reverse*10+digit
print(reverse)

num2=reverse

y=int(input("Enter the digit of which position is to be found: "))

z=0
while(num2>0):
    z+=1
    digit3=num2%10
    num2=num2//10
    if(y==digit3):
        break
print(y,"is at position",z)