#Logical Operator Keywords

"""
This logical operator contains 5 words that return either True or False
They are 'and','or','not','in', 'is'
"""

name = "Solomon Bestz"
new_name = name


if new_name is name:
    # print("True")
    pass

"""
The 'is' keyword return True if a variable points to another variable
in the same memory location
new_name as the value of name which makes them point to the same 
memory location
"""

# Control Structure Keywords

"""
This keywords are used to start a conditional statement, they are 'if', 
'elif', and 'else'.
"""

color = "red"

if color == "black":
    print("Black")
elif color == "green":
    print("Green")
elif color == "red":
    print("red")
else:
    print("Color Not Found.")


