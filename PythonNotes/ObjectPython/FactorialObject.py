def factorial(fact):
    
    x=1
    for i in range(fact,0,-1):
        x*=i
    return x
fact=int(input("Enter Number to find factorial : "))
print(factorial(fact))
