a=81
x=0
for i in range(1,a+1):
    if(a%i==0):
        x=i*i
        y=i
    elif(x==a):
        print(y)
        break        
