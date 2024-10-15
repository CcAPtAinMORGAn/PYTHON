# Open the file in append mode to add new contacts
file = open("phonediary.txt", "a")
contact = input("Enter Contact Number: ")

# Check if the contact number is 10 digits
if len(contact) == 10:
    # Check if the first digit is '9'
    if contact[0] == '9':
        name = input("Enter any Name: ")
        file.write("Name: ")
        file.write(name)
        file.write("\n")
        file.write("Contact: ")
        file.write(contact)
        file.write("\n")
        file.write("------------------------------\n")
    else:
        print("Enter a number starting with 9.")
else:
    print("Enter only a 10-digit number.")

# Close the file after writing
file.close()

# Now read the file and print its contents
with open("phonediary.txt", "r") as fo:
    content = fo.read()
    print(content)

# Truncate the file (clear its contents)
with open("phonediary.txt", "w") as fo:
    pass  # This clears the file
