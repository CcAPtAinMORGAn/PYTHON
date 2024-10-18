str1 = "this is string example....wow!!!"
str2 = "exam"
#  0 indexing
print(str1.find(str2))  
# Finds the first occurrence of 'exam'
print(str1.find(str2, 10))  
# Finds 'exam' starting from index 10
print(str1.find(str2, 40)) 
# Attempts to find 'exam' starting from index 40
