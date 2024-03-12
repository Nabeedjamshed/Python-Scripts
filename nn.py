def get_coffee_type():
    coffee_type = input("Enter the type of coffee (B for Black and W for White): ")
    return coffee_type

def get_cup_size():
    cup_size = input("Is the cup size double? (Y/N): ")
    return cup_size

def g_coffee_type():
    coffee_type = input("Is the coffee manual? (Y/N): ")
    return coffee_type

def compute_time(coffee_type, cup_size, is_manual):
    if coffee_type == "B":
        if is_manual == "Y":
            time = 10
        else:
            time = 5
    else:
        if is_manual == "Y":
            time = 15
        else:
            time = 7.5

    if cup_size == "Y":
        time *= 1.5

    return time

coffee_type = get_coffee_type()
cup_size = get_cup_size()
is_manual = g_coffee_type()

time = compute_time(coffee_type, cup_size, is_manual)

print(f"Type of coffee: {'Black' if coffee_type == 'B' else 'White'}")
print(f"Cup size: {'Double' if cup_size == 'Y' else 'Single'}")
print(f"Coffee type: {'Manual' if is_manual == 'Y' else 'Automatic'}")
print(f"Coffee time: {time} minutes")


