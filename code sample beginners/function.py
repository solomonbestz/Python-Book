# FUNCTION

# def house(location, owner):
#     print(f"The house is at {location} and {owner} is the owner")

# def greet_user(user_name):
#     print(f"Welcome {user_name}")

# def keyword_arg(**grades):
#     for name, grade in grades.items():
#         print(f"{name} = {grade}")

# def arguments(*args):
#     result = 0 
#     for n in args:
#         result += n
#     return result

def max_func(num1, num2):
    if num1 > num2:
        return True
    else:
        return False

if __name__=='__main__':
    num1 = 19
    num2 = 20

    check_max = max_func(num1, num2)
    print(check_max)
    