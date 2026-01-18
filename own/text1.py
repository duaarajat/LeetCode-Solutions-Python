"""Task: Create a text file hello.txt and write the string "Hello, File Handling in Python!" to it. Then read it and print the contents."""

text = "Hello, File Handling in Python!"
file_path = "own/hello.txt"
f = open(file_path, 'w')
f.write(text)
f.close()
f = open(file_path, 'r')
print(f.read())