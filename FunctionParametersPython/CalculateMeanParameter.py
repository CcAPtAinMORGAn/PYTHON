import math

def Calculate_Mean(number1,number2,number3,number4):
    
    numbers = [number1, number2, number3, number4]
    return (sum(numbers)/len(numbers))

number1 = 7
number2 = 5
number3 = 6
number4 = 8

Mean = Calculate_Mean(number1,number2,number3,number4)

print(f"The Mean of {number1,number2,number3,number4} is {Mean}") 