try:
   file=open("mydata.txt","r")
   print(file.read())
   file.close()
except FileNotFoundError:
    print("File Does Not Exist")



# # output
# File Does Not Exist
