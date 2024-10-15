file=open("phonediary.txt","a")
contact=input("Enter Contact Number:")
if(len(contact)==10):
    name=input("Enter any Name:")
    file.write("Name:")
    file.write(name)
    file.write("\n")
    file.write("Contact:")
    file.write(contact)
    file.write("\n")
    file.write("------------------------------\n")
else:
    print("Enter only 10 digit")
    
file.close()

fo = open("phonediary.txt", "r")
print(fo.read())
