# num=int(input("ENTER NUMBER: "))
# reverse=0
# copy=num

# while(copy>0):
#     digit=copy%10
#     reverse=reverse*10+digit
#     copy=copy//10

# if (reverse==num):
#     print(num,"is a palindrome number.")
# else:
#     print(num,"is not a Palindrome number.")
# *********************************************************************#

# Print palindrome from 0 to n numbers
Number=int(input("Enter Number: "))

for i in range (0,Number+1):
    a=0
    Temp=i
    while(Temp>0):
        remainder=Temp%10
        a=remainder+(a*10)
        Temp=Temp//10

    if(a==i):
        print(i," is a Palindrome number.")