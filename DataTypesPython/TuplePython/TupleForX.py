# thistuple = ("apple", "banana", "cherry")
# for x in thistuple[0]:
#  print(x,end='')

##This print index 1 and 2, index 0 is left out
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple[1:]:
#  print(x)

##This will print index 0 and 1,index 2 will be left out
thistuple = ("apple", "banana", "cherry")
for x in thistuple[:2]:
 print(x)

##This will print index 2 and 0,all other index will be left out
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple[::2]:
#  print(x)

##This will print index 0 and 1,it prints in range of for loop which is taken as -1
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple[0:2]:
#  print(x)

##This prints the tuple in reverse
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple[::-1]:
#  print(x)