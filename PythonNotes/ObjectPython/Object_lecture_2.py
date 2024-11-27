
class myclass:
  def prime(self):
    x = 10
    
    
    b = 0 
    
    for i in range(1,x + 1):
      if(x % i == 0):
        b += 1
    
    if(b == 2):
      return x ,"is prime"
    else:
      return x,"is not prime"
    
p1 = myclass()

print(p1.prime()



class myclass:
  def __init__(self,x):
    
    self.b = 0
    for i in range(1,x + 1):
      if(x % i == 0):
          self.b+=1  
    
    if(self.b == 2):
      print(x,"is prime number")
    else:
      print(x,"is non prime number")
    
    
    
p1 = myclass(8)


print("No. of divisors that give remainder zero is ",p1.b)
  
