# PYTHON MODULE

from calculation import add_calc

if __name__=="__main__":
    # print(add_calc(34, 50))
    pass


# RANDOM MODULE 

# import random


# if __name__=='__main__':

#     my_list = [1, 2, 6, 5, 9, 3]

#     rand_item = random.choice(my_list)
#     print(rand_item)

#     rand_num = random.randint(1, 10)

#OS MODULE

from os import system

if __name__=='__main__':
    print("Playing with the system method")

    user_input = input("Do you want to clear screen?: ")

    if user_input.lower() == "yes":
        system('cls')
        print('We have cleared the screen')
    else:
        print("You don't want to clear the screen.")


