# Open a file
fo = open("yash.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")
# Close opend file
fo.close()

#Read created file 
fo = open("yash.txt", "r")
print(fo.read())