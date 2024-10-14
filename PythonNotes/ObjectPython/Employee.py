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