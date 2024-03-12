def coffee_machine():
    coffee_type = input("Enter the type of coffee (B for Black and W for White): ")
    cup_size = input("Is the cup size double? (Y/N): ")
    is_manual = input("Is the coffee manual? (Y/N): ")
    if coffee_type == "B":
        print("Black coffee selected.")
        put_water(20 if cup_size == "Y" else 15)
        put_sugar(20 if cup_size == "Y" else 15)
        mix_well(25 if cup_size == "Y" else 20)
        add_coffee(15 if cup_size == "Y" else 2)
    elif coffee_type == "W":
        print("White coffee selected.")
        put_water(15 if cup_size == "Y" else 10)
        put_sugar(15 if cup_size == "Y" else 10)
        mix_well(20 if cup_size == "Y" else 15)
        add_coffee(2)
        add_milk(4)
    else:
        print("Invalid input. Please enter B or W for coffee type.")
        return

def put_water(time):
    print(f"Put water in the machine. Time taken: {time} minutes.")

def put_sugar(time):
    print(f"Put sugar in the machine. Time taken: {time} minutes.")

def mix_well(time):
    print(f"Mix the ingredients well. Time taken: {time} minutes.")

def add_coffee(time):
    if input("Is the coffee size double? (Y/N): ") == "Y":
        time *= 1.5
    print(f"Add coffee to the machine. Time taken: {time} minutes.")

def add_milk(time):
    print(f"Add milk to the machine. Time taken: {time} minutes.")

coffee_machine()
