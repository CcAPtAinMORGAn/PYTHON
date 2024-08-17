a=3
b=0
for i in range (1,a+1):
    if(a%i==0):
        b+=1
if(b==2):
    print(a," is a prime number") 
else:
    print(a," is not a prime number")

"""
Num=int(input("Enter Number"))

for i in range (1,Num+1):
    b=0
    for j in range (1,i+1):
        if(i%j==0):
            b+=1    
    if(b==2):
        print(i," is a prime number")
        
"""