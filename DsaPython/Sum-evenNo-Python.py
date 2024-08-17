n=int(input("Enter Number"))
Sum=0

for i in range (1,n+1):
    if(i%2==0):
        Sum+=i
print(Sum)