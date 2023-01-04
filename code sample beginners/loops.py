# LOOPS

"""
INTRO TO LIST
"""
"""
In our street variable we have three houses, 
say I boarded a bike going to house3 i wont be 
able to get to house3 if i don't know the address and in our case our
house numbering starts from index 0
"""
"""
Getting the house isn't difficult, we just need to 
call the variable and place in the number in a square bracket 
and we can access the house that way..
"""

# street = ['house1', 'house2', 'house3']

# for house in street:
#     print(house)

"""
The above loop we have written would print out all the houses in our
street list
"""


numbers = [4, 6, 7, 8, 9, 12, 71, 2, 10, 1]
sum_number = 0

for number in numbers:
    sum_number = sum_number + number

# print(sum_number)

# WHILE LOOP 

initial = 0

end_loop = 10

while initial < end_loop:
    # print(initial)
    initial = initial + 1
    

#GUESS GAME

secret_number = 8
start_game = 0
stop_game = 5

print("Guess My Secret Number")

while start_game < stop_game:
    user_input = int(input("Enter Number: "))

    if user_input == secret_number:
        print("You Won!!! Genius")
        break
    else:
        if (stop_game-1)-start_game != 0 and (stop_game-1)-start_game != 1:
            print(f"Try Again, {(stop_game-1)-start_game} guesses left")
        elif (stop_game-1)-start_game == 1:
            print(f"Try Again, {(stop_game-1)-start_game} guess left")
        else:
            print(f"{(stop_game-1)-start_game} guess left")
    start_game = start_game + 1
else:
    print("Game Over!!! You Lost")
