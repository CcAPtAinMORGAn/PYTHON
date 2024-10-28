dict = {'Name': 'Zara', 'Age': 7, 'Roll id' : 23}
print ("Value : " , dict.setdefault('Age', None))
print ("Value : " , dict.setdefault('Roll id', None))
print ("Value : " , dict.setdefault('Gender', None))
print (dict)

# Practical use 1 
# counts = {}
# items = ['apple', 'banana', 'apple', 'orange']

# for i in items:
#     counts.setdefault(i, 0)  # Initialize key with 0 if it doesn't exist
#     counts[i] += 1

# print(counts)  

# Practical use 2 
# nested_dict = {}
# for category, item in [('fruits', 'apple'), ('fruits', 'banana'), ('vegetables', 'carrot')]:
#     nested_dict.setdefault(category, []).append(item)

# print(nested_dict)  

config = {'timeout': 30}
config.setdefault('timeout', 60)  # Will not overwrite existing value
config.setdefault('retries', 3)    # Will add 'retries' key with a default value

print(config)  # Output: {'timeout': 30, 'retries': 3}

