# 1. List is a collection which is ordered and changeable. Allows duplicate members

# mylist = ['apple','mango','banana']
# print(mylist)


# list1 = ["abc", 34, True, 40, "male"]
# print(list1)
# print(type(list1))

# thislist = ["apple", "banana", "cherry"]
#             #0        #1       #2
# print(thislist[1])

# list1 = ['cricket','chess', 'ludo']
# list1[1] = 'tennis'
# print(list1)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# # thislist.remove(thislist[1])
# print(thislist)

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