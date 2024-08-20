import math

def Calculate_StandardDeviation(number1,number2,number3,number4):
    
    numbers = [number1, number2, number3, number4]

    n=len(numbers)

    Mean=(sum(numbers)/n)

    squared_difference= [(x - Mean) ** 2 for x in numbers]

    variance=sum(squared_difference)/n

    StandardDeviation=math.sqrt(variance)

    
    return StandardDeviation 

number1 = 7
number2 = 5
number3 = 6
number4 = 8

SD=Calculate_StandardDeviation(number1,number2,number3,number4)

print(f"The Standard Deviation of {number1,number2,number3,number4} is {SD}") 
