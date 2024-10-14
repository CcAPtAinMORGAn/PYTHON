def prime(n):
    if(n==1 or n==2):
        print("prime number")
    i=2
    while(n>i):
        if(n%i==0):
            print("No Prime Number")
            break
        i=i+1
    if(n==i):
        print("Number is prime")


n=int(input("Enter any number"))
prime(n)
