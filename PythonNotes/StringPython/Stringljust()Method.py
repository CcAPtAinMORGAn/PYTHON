str = "this is string example....wow!!!"
print(str.ljust(50, '*'))  
# Pads the string on the right with '*'

# Practical use 
data = [("Name", "Age", "City"), ("Alice", 30, "New York"), ("Bob", 25, "Los Angeles")]
widths = [10, 5, 15]

for row in data:
    print(row[0].ljust(widths[0]), row[1], str(row[2]).ljust(widths[2]))
