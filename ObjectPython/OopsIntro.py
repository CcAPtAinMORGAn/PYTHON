#oops (Object oriented programming system)
# class is collection of function and variable

class sample:
    def input(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        self.c=self.a+self.b
        print("Total sum is ",self.c)
    def minus(self):
        self.c=self.a-self.b
        print("Total minus is ",self.c)
    def multiply(self):
        self.c=self.a*self.b
        print("Total sum is ",self.c)
    def divide(self):
        self.c=self.a/self.b
        print("Total sum is ",self.c)


#Create an object

ob=sample()  #create object

ob.input(10,4)
ob.add()
ob.minus()
ob.multiply()
ob.divide()
