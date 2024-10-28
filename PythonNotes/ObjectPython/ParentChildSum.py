class A:
    def getA(self,a):
        self.a=a
class B(A):
    def getB(self,b):
        self.b=b
    def sum(self):
        self.c=self.a+self.b
        print("Total sum is :",self.c)
ob=B()
ob.getA(10)
ob.getB(10)
ob.sum()
