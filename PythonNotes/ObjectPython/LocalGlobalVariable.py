total=10  #global

def show(total):
    print("local",total)  #local variable


show(total=1)
print("Global:",total)

sum = lambda a,b : a + b

print(sum(5,6))
