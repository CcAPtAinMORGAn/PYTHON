
file=open("mark.txt","a")
rollno=int(input("Enter Rollno :"))
file.write("Rollno:");
file.write(str(rollno))
file.write("\n")

name=input("Enter any Name:")
file.write("Name:");
file.write(name)
file.write("\n")

math=int(input("Enter marks in math"))
file.write("Math:");
file.write(str(math))
file.write("\n")

sci=int(input("Enter marks in sci"))
file.write("Sci:");
file.write(str(sci))
file.write("\n")

eng=int(input("Enter marks in eng"))
file.write("eng:");
file.write(str(eng))
file.write("\n")

tot=math+sci+eng
file.write("Obtained:");
file.write(str(tot))
file.write("/300")
file.write("\n")

per=tot/3
file.write("Per:");
file.write(str(per))
file.write("%")
file.write("\n")

file.write("\n---------------------\n");

file.close()
fo = open("mark.txt", "r")
print(fo.read())
