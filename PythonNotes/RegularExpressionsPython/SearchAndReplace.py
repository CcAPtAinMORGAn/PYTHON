import re
phone = "2004-959-559 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)

# Pattern Breakdown:
#: Matches the # character.
# .*: Matches any character (.) zero or more times (*), effectively capturing everything that follows the #.
# $: Asserts the position at the end of the string (or end of the line in multiline mode).


print ("Phone Num : ", num)


num = re.sub(r'\D', "", phone)

# This function is used to replace occurrences of a pattern in a string with a specified replacement. It takes three main arguments:
# The pattern to search for (in this case, r'\D').
# The replacement string (in this case, an empty string "").
# The input string where the substitution should occur (in this case, phone).
# r'\D':

# This is the regular expression pattern being used. The r indicates that it's a raw string, which means backslashes are treated literally.
# \D: This is a shorthand character class that matches any character that is not a digit (0-9). It effectively captures everything that is not a number.
print ("Phone Num : ", num)
