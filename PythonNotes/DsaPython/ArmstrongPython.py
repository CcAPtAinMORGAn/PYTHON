# Number=int(input("Enter Number"))
# numberOfDigits = len(str(Number))
# Sum=0
# Temp=Number

# while (Temp > 0):
#     remainder = Temp % 10
#     Sum += remainder ** numberOfDigits
#     Temp = Temp // 10

# if (Sum == Number):
#     print(Number," is an Armstrong number.")   	
# else:
#     print(Number," is not an Armstrong number.")


Number=int(input("Enter Number"))

for i in range (1,Number+1):
    numberofDigits=len(str(i))
    Sum=0
    Temp=i
    while(Temp>0):
        remainder=Temp%10
        Sum+=remainder**numberofDigits
        Temp = Temp // 10
    if(Sum==i):
        print(i," is an Armstrong Number.")
    # else:
    #     print(i," is not an Armstrong Number.")