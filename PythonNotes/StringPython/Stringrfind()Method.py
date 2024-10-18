str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rfind(str2))
print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))
# rfind() searches for the last occurrence of str2 ("is") in str1.
# It returns the index of the last occurrence or -1 if not found.
# In this case, it would return 5 because the last "is" appears at
# that position

# It returns the index of the last occurrence or -1 if not found. 
