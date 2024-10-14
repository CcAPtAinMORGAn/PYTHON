import os
os.remove("yash.txt")

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

# Example
# Check if file exists, then delete it:

import os
if os.path.exists("yash.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
# Delete Folder
# To delete an entire folder, use the os.rmdir() method:

# Example
# Remove the folder "myfolder":

import os
os.rmdir("myfolder")
# Note: You can only remove empty folders.
