Str='this is string example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))

print (Str.endswith(suffix,20))
# print(Str.endswith(suffix, 20)): Checks if the substring
# starting from index 20 to the end ends with '!!' → Output:
# True

suffix='exam'
print (Str.endswith(suffix))

print (Str.endswith(suffix, 0, 19))
# print(Str.endswith(suffix, 0, 19)): Checks if the substring
# from index 0 to 19 ends with 'exam'-output true
