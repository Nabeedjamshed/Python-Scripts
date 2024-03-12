import random
user_choice = input("Enter Gun, Snake or Water: ")
l = ['Gun','Snake','Water']
print("Your choice: ",user_choice)
computer_choice  = random.choice(l)
print("Computer choice: ",computer_choice)
if(user_choice == computer_choice):
    print("Draw")
elif((user_choice == 'Gun' and computer_choice == 'Snake') or (user_choice == 'Water' and computer_choice == 'Gun') or (user_choice == 'Snake' and computer_choice == 'Water')):
    print("You Win")
else:
    print("Computer Win")