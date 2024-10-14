# Open a file
fo = open("yash.txt", "w")
fo.write( "C++\nJava\nPython\nPerl\nPHP")
# Added a newline at the end


# Close the file after reading
fo = open("yash.txt", "r")
print ("Name of the file: ", fo.name)
for index in range(5):
 line = next(fo)
 print ("Line No %d - %s" % (index, line))
# Close opened file
fo.close()

