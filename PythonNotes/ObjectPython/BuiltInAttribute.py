class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee:", Employee.empCount)

    def displayEmploe(self):
        print("Name:", self.name, ", Salary:", self.salary)

# Creating instances of Employee class
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

# Display employee information
emp1.displayEmploe()  
#Anything can be written instead of displayEmploe
emp2.displayEmploe() 


emp1.displayCount()  

# Printing class information
print("Employee.__doc__:", Employee.__doc__)               
# Documentation string
print("Employee.__name__:", Employee.__name__)             
# Class name
print("Employee.__module__:", Employee.__module__)         
# Module name
print("Employee.__bases__:", Employee.__bases__)           
# Base classes
print("Employee.__dict__:", Employee.__dict__)             
# Class attributes and methods
