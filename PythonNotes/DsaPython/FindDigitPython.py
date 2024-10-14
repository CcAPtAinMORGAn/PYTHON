Num=int(input("Enter Number: "))
LastDigit=Num%10
print(LastDigit," is the  Last Digit.")

reverse=0
copy=Num

while(copy>0):
    digit=copy%10
    copy=copy//10
    reverse=reverse*10+digit
x=int(input("Enter Digit you want to Find: "))

Digit=(reverse%(10**x))  //  ((10**x)//10)

print(Digit," is the",x,"th Digit.")





# Num=int(input("Enter Number"))

# LastDigit=Num%10
# print(LastDigit," is the Last Digit.")

# while(Num>=10):
#     Num=Num//10
#     FirstDigit=Num
# print(FirstDigit," is the First Digit.")


