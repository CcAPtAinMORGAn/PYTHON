try:
    a=int(input("Enter any number: "))
    b=int(input("Enter any number: "))
    c=a/b
    print("Result:",c)
except ZeroDivisionError:
    print(a,"Is Not Divisible By Zero")
except ValueError:
    print("Enter Numerical Values")


# # output
# Enter any number: a
# Enter Numerical Values
