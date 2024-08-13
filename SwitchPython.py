"""
n=int(input("Enter any number [1-7]"))
match n:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case default:
        print("Invalid Option")
"""

n=int(input("Enter 1 for Multiply, 2 for Divide, 3 for Add, 4 for Subtract"))

match n:
    case 1:
        a=int(input("Enter number a for Multiplication"))
        b=int(input("Enter number b for Multiplication"))
        print("Multiply",a*b)
    case 2:
        a=int(input("Enter number a for Division"))
        b=int(input("Enter number b for Division"))
        print("Division",a/b)
    case 3:
        a=int(input("Enter number a for Addtion"))
        b=int(input("Enter number b for Addtion"))
        print("Addtion",a+b)
    case 4:
        a=int(input("Enter number a for Subraction"))
        b=int(input("Enter number b for Subraction"))
        print("Subraction",a-b)
    