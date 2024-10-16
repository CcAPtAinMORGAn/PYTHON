# The fabs() method returns the absolute value of x. Although similar to the abs() function,
# there are differences between the two functions. They are-
#  abs() is a built in function whereas fabs() is defined in math module.
#  fabs() function works only on float and integer whereas abs() works with complex
# number also.

import math # This will import math module
print ("math.fabs(-45.17) : ", math.fabs(-45.17))
print ("math.fabs(100.12) : ", math.fabs(100.12))
print ("math.fabs(100.72) : ", math.fabs(100.72))
print ("math.fabs(math.pi) : ", math.fabs(math.pi))
