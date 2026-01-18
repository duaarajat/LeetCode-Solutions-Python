"""Task: Write a list of strings (lines) to a file called poem.txt. Then read the file line by line and print each line."""

text = """Twinkle
Twinkle 
little star
how are you
and what you are
up upon the world so high
like a diamond in the sky."""

file_path = "own/poem.txt"

f = open(file_path, 'w')
f.write(text)
f.close()
f = open(file_path, 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()