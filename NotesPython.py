st="Python"
for i in st:
    if(i=='h'):
        break  #to terminate
    print(i)

print("Continue:")
st="Python"

for i in st:
    if(i=='h'):
        continue   #skip
    print(i)

st="Python"
print("data:", st[4:6])



st="python"

for i in st:

    print(i)



#break statement



print("break")

for i in st:

    if(i=='h'):

        break

    print(i)



#continue

print("continue.")

for i in st:

    if(i=='h'):

        continue

    print(i)



#pass

print("pass")

for i in st:

    if(i=='h'):

        print("Pass")

        pass

    print(i)





print("")

for i in range(1,31):

    if(i>=10 and i<=20):

        continue

    print(i,end=' ')



class Emp:
    def getdata(self, empno,ename,salary):
        self.empno=empno
        self.ename=ename
        self.salary=salary
    def show(self):
        print("Empno:", self.empno)
        print("Emp Name:", self.ename)
        print("Salary:", self.salary)

E1=Emp()
E1.getdata(1,"Amit",45000)
E1.show()

E2=Emp()
E2.getdata(2,"Suraj",46000)
E2.show()

E3=Emp()
E3.getdata(3,"Zulkar",55000)
E3.show()
         

#Addition two number
import math
print("Pow",math.pow(2,5))
a=10
b=20
print("a=",a)
print("b=",b)



i=10
while(i>=1):
    print(i, end=' ')
    i=i-1

