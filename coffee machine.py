def get_coffee_type_size():
    time = 0
    dic1 = {'Put Water': 15, 'Add Sugar': 15, 'Mix Well': 20, 'Add Coffee': 2, 'Add Milk': 4}
    dic2 = {'Put Water': 20, 'Add Sugar': 20, 'Mix Well': 25, 'Add Coffee': 15, 'Add Milk': 0}
    type = input("Enter the type of coffee (B for Black and W for White): ")

    size = input("Is the cup size double? (Y/N): ")
    full_foam = input("Enter in full foam White coffee OR Black coffee: ")
    manual = input("Is the coffee manual? (Y/N): ")

    print("--------------------------------------")
    print(f"Operation\t\t\t\t{full_foam}")
    print("--------------------------------------")
    if type == "W":
        if size == "Y":
            for key, value in dic1.items():
                print(key, "\t\t\t\t", value * 1.5, "minutes")
                time = time + value * 1.5
                if manual == "Y":
                    input()
        else:
            for key, value in dic1.items():
                print(key, "\t\t\t\t", value * 1.5, "minutes")
                time = time + value
                if manual == "Y":
                    input()
    elif type == "B":
        if size == "Y":
            for key, value in dic2.items():
                print(key, "\t\t\t\t", value * 1.5, "minutes")
                time = time + value * 1.5
                if manual == "Y":
                    input()
        else:
            for key, value in dic2.items():
                print(key, "\t\t\t\t", value, "minutes")
                time = time + value
                if manual == "Y":
                    input()
    else:
        print("Invalid Input")
    print("--------------------------------------")
    print("Hurrah! Your coffee is ready in ", time, "minutes")


get_coffee_type_size()

# DISPLAY ("Enter your name: ")
# name <- INPUT ()
# DISPLAY ("Hello, " + name)

# name <- INPUT("Enter your name: ")
# age <- INPUT("Enter your age: ")
# message <- f"Hello, {name}. You are {age} years old."
# DISPLAY(message)


# Define a function called get_coffee_type_size
#     Initialize a variable called time to zero
#     Initialize a dictionary called dic1 with the following key-value pairs:
#         Put Water: 15
#         Add Sugar: 15
#         Mix Well: 20
#         Add Coffee: 2
#         Add Milk: 4
#     Initialize a dictionary called dic2 with the following key-value pairs:
#         Put Water: 20
#         Add Sugar: 20
#         Mix Well: 25
#         Add Coffee: 15
#         Add Milk: 0
#     Ask the user to enter the type of coffee (B for Black and W for White) and store it in a variable called type
#     Ask the user if the cup size is double (Y/N) and store it in a variable called size
#     Ask the user to enter in full foam White coffee OR Black coffee and store it in a variable called full_foam
#     Ask the user if the coffee is manual (Y/N) and store it in a variable called manual
#     Display a line of dashes
#     Display the word Operation followed by a tab and the value of full_foam
#     Display another line of dashes
#     If type is equal to W
#         If size is equal to Y
#             For each key and value in dic1
#                 Display the key followed by a tab and the value multiplied by 1.5 and the word minutes
#                 Add the value multiplied by 1.5 to time
#                 If manual is equal to Y
#                     Wait for the user to press a key
#         Otherwise
#             For each key and value in dic1
#                 Display the key followed by a tab and the value and the word minutes
#                 Add the value to time
#                 If manual is equal to Y
#                     Wait for the user to press a key
#     Otherwise if type is equal to B
#         If size is equal to Y
#             For each key and value in dic2
#                 Display the key followed by a tab and the value multiplied by 1.5 and the word minutes
#                 Add the value multiplied by 1.5 to time
#                 If manual is equal to Y
#                     Wait for the user to press a key
#         Otherwise
#             For each key and value in dic2
#                 Display the key followed by a tab and the value and the word minutes
#                 Add the value to time
#                 If manual is equal to Y
#                     Wait for the user to press a key
#     Otherwise
#         Display the message Invalid Input
#     Display another line of dashes
#     Display the message Hurrah! Your coffee is ready in followed by the value of time and the word minutes
#
# Call the function get_coffee_type_size

