# Syntax Error

# print(Welcome To Bestz World)

# CATCH EXCEPTION

if __name__=="__main__":
    print("Calculator")
    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        answer = num1 + num2
        print(f"The Answer is: {answer}")
    except ValueError:
        raise ValueError("You should type in a number not an alphabet")




