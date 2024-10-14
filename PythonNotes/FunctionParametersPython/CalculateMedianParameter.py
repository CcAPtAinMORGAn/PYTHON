def Calculate_Median(number1, number2, number3, number4):
    numbers = [number1, number2, number3, number4]

    numbers.sort()  # Sort the numbers in ascending order
    
    ## 5, 6, 7, 8 Number 1 and 2 will be at the center of the sorted list.
    ## Thus Median Will be the average of ((6+7)/2)

    median = (numbers[1] + numbers[2]) / 2  # Average the two middle numbers
    return median

number1 = 6
number2 = 8
number3 = 5
number4 = 7

Median = Calculate_Median(number1, number2, number3, number4)

print(f"The Median of {number1, number2, number3, number4} is {Median}")
