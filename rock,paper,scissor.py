import random

user_choice = input("ENTER USER CHOICE: ")
inputs = ["rock","paper","scissor" ]

computer_choice = random.choice(inputs)

if (user_choice == 'rock' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'scissor') or (user_choice == 'scissor' and computer_choice == 'rock'):
    print(f"Computer choose:{computer_choice}. Computer wins")
elif user_choice == computer_choice:
    print("Match Draws!")
else:
    print("User wins")