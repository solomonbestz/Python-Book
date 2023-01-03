# FUNCTION

# def house(location, owner):
#     print(f"The house is at {location} and {owner} is the owner")

# def greet_user(user_name):
#     print(f"Welcome {user_name}")

def keyword_arg(**grades):
    for name, grade in grades.items():
        print(f"{name} = {grade}")

if __name__=='__main__':
    students = {'solomon':2.5, 'david':3.4, 'daniel':3.0}
    keyword_arg(**students)