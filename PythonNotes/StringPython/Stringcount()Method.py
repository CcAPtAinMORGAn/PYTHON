str="this is string example....wow!!!"
sub='i'
print ("str.count('i') : ", str.count(sub))
sub='exam'
print ("str.count('exam', 10, 40) : ", str.count(sub,10,40))

# So, in your example with str.count('exam', 10, 40), it counts
# how many times 'exam' appears in the substring of str starting
# from index 10 up to (but not including) index 40.
# If the length of str is less than 40, it will only count
# occurrences up to the end of the string.



