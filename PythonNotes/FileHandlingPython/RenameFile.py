import os
# Rename a file from test1.txt to test2.txt
os.rename( "yash.txt", "yashv.txt" )


#Read created file 
fo = open("yashv.txt", "r")
print(fo.read())
