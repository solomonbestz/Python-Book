# OPENING FILE

file_object = open("code sample beginners/test.txt", "r")
file_object.close()
print(f"""
File Name: {file_object.name}
File Mode: {file_object.mode}
File Closed?: {file_object.closed}
""")



"""
We can name the file_object any other name, the text.txt is the file
and it is located in the same path as our file.py file.
The r is telling the interpreter we are reading the file.
"""


