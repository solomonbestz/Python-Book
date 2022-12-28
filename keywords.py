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

# if color == "black":
#     print("Black")
# elif color == "green":
#     print("Green")
# elif color == "red":
#     print("red")
# else:
#     print("Color Not Found.")


# Iteration Keywords

"""
The Iteration keywords are used in looping through collection of items, let's take a look
at for, while, break, continue, else
"""

my_list = [ 1, 2, 3, 4, 5, 6]
count = 1

while len(my_list) > 7:
    print(count)
    count += 1
else:
    print("Our While condition wasn't met.")

