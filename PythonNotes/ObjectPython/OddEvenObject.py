# def print_even_numbers():
#     for num in range(1, 101):  # Loop through numbers from 1 to 100
#         if num % 2 == 0:  # Check if the number is even
#             print(num)

# # Call the function
# print_even_numbers()


# def print_even_numbers():
#     for num in range(start,end+1):  # Loop through numbers from 1 to 100
#         if num % 2 == 0:  # Check if the number is even
#             print(num)
# start=int(input("Enter Start: "))
# end=int(input("Enter End:  "))

# print_even_numbers()


def oddEven(x):
    if(x%2!=0):
        return f"{x} is odd"
    else:
        return f"{x} is even"
    
x=int(input("Enter Number to find odd: "))
print(oddEven(x))   
