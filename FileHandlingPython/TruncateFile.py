# Open a file in write mode and write some content
fo = open("example.txt", "w")
fo.write("Hello, World!\nThis is a test file.")
fo.close()

# Open the file in read/write mode
fo = open("example.txt", "r+")
fo.seek(12)  # Move the pointer to the 6th byte
fo.truncate()  # Truncate the file from this position
fo.close()

# Read and print the remaining content
fo = open("example.txt", "r")
print(fo.read())  # Output: Hello,
fo.close()
# Writing Content: The file is created and some text is written to it.
# Seeking and Truncating: The file is opened again in read/write mode, the file pointer is moved to the 6th byte, and the file is truncated from that position.
# Reading the Content: Finally, the file is opened in read mode to display the remaining content, which will show only "Hello," after the truncation.
