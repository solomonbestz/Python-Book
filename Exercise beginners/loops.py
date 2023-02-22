# Write a program to keep asking for a number
# until you enter a negative number. 
# At the end, print the sum of all entered numbers

# list_numbers = []
# sum_number = 0

# while True:
#     user_number = int(input("Enter Number: "))
#     if user_number < 0:
#         for number in range(len(list_numbers)):
#             sum_number = sum_number + list_numbers[number]
#         print(f"Sum of positive numbers: {sum_number}")
#         break
#     else:
#         list_numbers.append(user_number)


# Write a program to ask for a name until the user enters END. 
# Print the name each time. When you are done, print "I am done."

# list_of_names = []

# while True:
#     user_input = input("Enter Name: ")

#     if user_input == "END":
#         for name in list_of_names:
#             print(name)
#         print('I am done')
#         break
#     else:
#         list_of_names.append(user_input)

# Write a program to find the multiples of n,
# your loop should iterate 10 times.

user_input = int(input("Enter Number: "))

for n in range(1, 10):
    multiples = user_input * n
    print(multiples)
    
