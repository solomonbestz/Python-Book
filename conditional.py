# CONDITIONAL STATEMENT

"""
Let's work with the if else conditional statement 
"""

num_1 = 200
num_2 = 400
operator = '-'

if operator == '+':
    answer = num_1 + num_2
    print(f'Answer: {answer}')
elif operator == '-':
    answer = num_1 - num_2
    print(f"Answer: {answer}")
elif operator == '*':
    answer = num_1 * num_2
    print(f"Answer {answer}")
elif operator == "/":
    answer = num_1 / num_2
    print(f"Answer {answer}")
else:
    print(f"{operator} is an invalid operator")


# EXAMPLES OF BLOCK OF CODE AND INDENTATION
"""
I would give you a simple example of a block
"""

if "S" in "Solomon":
    print("Yes")


def my_name():
    print("Welcome Solomon Bestz")

"""
The two examples above are blocks of code and a colon is placed at the front of an expression then
the indentation follows the next line. Without the colon the block is void.
"""