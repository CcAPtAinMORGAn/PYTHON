class myclass:
    x = 5
p1 = myclass()
print(p1.x)

#-------------------------------------------------------------------------
#class myclass:
#     x = 5
#     y = 10
#     z = x + y
#p1 = myclass()
#print(p1.z)

#-------------------------------------------------------------------------

#class myclass:
#     x = []
#     for i in range(1,11):
#         x.append(i)   
#p1 = myclass()
#print(p1.x)

#-------------------------------------------------------------------------

#class myclass:
#     x = 0
#     for i in range(1,11):
#         x+=i   
#p1 = myclass()
#print(p1.x)

#-------------------------------------------------------------------------

#class myclass:
#     z = 5
#     x = 1
#     for i in range(1,z + 1):
#         x*=i   
#p1 = myclass()
#print(p1.x)

#-------------------------------------------------------------------------

#class myclass:
#     x = []
#     for i in range(1,11):
#         for j in range(1,11):
#             x.append(i)
#             x.append(j)
#             
#p1 = myclass()
#print(p1.x)


#-------------------------------------------------------------------------

#class myclass:
#    def variable(self):
#        x = 5
#        print(x)
#p1 = myclass()
#p1.variable()

#-------------------------------------------------------------------------

#class myclass:
#    def variable(self):
#        x = 5
#        return x
#        
#p1 = myclass()
#print(p1.variable())

#-------------------------------------------------------------------------

#class myclass:
#    def variable(self):
#        x = 5
#        y = 10
#        return x + y
#        
#p1 = myclass()
#print(p1.variable())

#-------------------------------------------------------------------------


#class myclass:
#    def variable(self):
#        for i in range(1,11):
#            print(i)
#        
#p1 = myclass()
#p1.variable()

#-------------------------------------------------------------------------

#class myclass:
#    def variable(self):
#        for i in range(1,11):
#              for j in range(1,11):
#                print(i,j)
#        
#p1 = myclass()
#p1.variable()

#-------------------------------------------------------------------------

#class myclass:
#    def variable(self):
#        x=[]
#        for i in range(1,11):
#            x.append(i)
#        return x
#p1 = myclass()
#print(p1.variable())

#-------------------------------------------------------------------------

class myclass:
    def variable(self):
        x=[]
        for i in range(1,11):
            for j in range(1,11):
                x.append(i)
                x.append(j)
        return x
p1 = myclass()
print(p1.variable())


#-------------------------------------------------------------------------
class myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p1 = myclass("Alice" , 25)

print(p1.name)

#-------------------------------------------------------------------------


class myclass:
  def __init__(self,):
    self.x = 5
    
    
p1 = myclass()

print(p1.x)




#-------------------------------------------------------------------------


# class myclass:
#     def __init__(self,x):
#         self.x = x
#         self.i =[]
#         for i in range(1,11):
#             self.i.append(i)
# p1 = myclass(5)

# print(p1.x)
# print(p1.i)

#-------------------------------------------------------------------------















