# thislist = ["apple", "banana", "cherry"]
# for x in thislist[0]:
#  print(x,end='')

##This print index 1 and 2, index 0 is left out
# thislist = ["apple", "banana", "cherry"]
# for x in thislist[1:]:
#  print(x)

##This will print index 0 and 1,index 2 will be left out
# thislist = ["apple", "banana", "cherry"]
# for x in thislist[:2]:
#  print(x)

##This will print index 3 and 0
thislist = ["apple", "banana", "cherry", "pie"]
for x in thislist[::3]:
 print(x)


##This prints the list in reverse
# thislist = ["apple", "banana", "cherry"]
# for x in thislist[::-1]:
#  print(x)