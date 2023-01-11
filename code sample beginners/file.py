# OPENING FILE



file_object = open("code sample beginners/test.txt", "r")

lines = []
for line in file_object:
    lines.append(line)
file_object.close()

print(lines)



"""
We can name the file_object any other name, the text.txt is the file
and it is located in the same path as our file.py file.
The r is telling the interpreter we are reading the file.
"""


