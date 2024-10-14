numbers = [4, 2, 7, 3, 9, 1, 4, 6, 7, 5]

# Sort the list in ascending order
sorted_numbers = sorted(numbers)

# Reverse the list
reversed_numbers = sorted_numbers[::-1]

# Find the maximum and minimum numbers in the list
max_number = max(numbers)
min_number = min(numbers)
sum_number = sum(numbers)

# Remove duplicates from the list
unique_numbers = list(set(numbers))

print("Original list:", numbers)
print("Sorted list:", sorted_numbers)
print("Reversed list:", reversed_numbers)
print("Maximum number:", max_number)
print("Minimum number:", min_number)
print("Sum of numbers: ", sum_number) 
print("List without duplicates:", unique_numbers)