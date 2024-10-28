class A:
    def getA(self,a):
        self.a=a
class B(A):
    def getB(self,b):
        self.b=b
class C(B):
    def getC(self,c):
        self.c=c
class D(C):
    def sum(self):
        self.d=self.a+self.b+self.c
        print("Total of a,,b,c :",self.d)
ob=D() 
# Store class D in ob whcih also store A,B,C
ob.getA(10)
ob.getB(10)
ob.getC(10)
ob.sum() 
