try:
    a=int(input("Enter any number: "))
    b=int(input("Enter any number: "))
    c=a/b
    print("Result:",c)
except ZeroDivisionError:
    print(a,"Is Not Divisible By Zero")


# # Error solved
# Enter any number: 10
# Enter any number: 0
# 10 Is Not Divisible By Zero
