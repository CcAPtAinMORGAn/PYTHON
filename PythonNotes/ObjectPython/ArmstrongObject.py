def armstrong(x):
    a = x  # Make a copy of the input number to process
    y = 0  # This will store the sum of the powers of the digits
    length = len(str(x))  # Number of digits in the number
    
    while a > 0:
        z = a % 10  # Get the last digit of 'a'
        y += z ** length  # Add the digit raised to the power of the number of digits
        a = a // 10  # Remove the last digit
    
    if y == x:  # Check if the sum equals the original number
        return f"{x} is an Armstrong number"
    else:
        return f"{x} is not an Armstrong number"

# Test the function with an example
x = 153
print(armstrong(x))
