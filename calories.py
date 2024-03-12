def calculate_calories_of_fat():
    total_calories = float(input("Enter total number of of calories: "))
    fat_grams = float(input("Enter fat gram in a food: "))
    calories_from_fat = fat_grams * 9
    if calories_from_fat > total_calories:
        print("Error: either the calories or fat grams were incorrectly entered.")
    else:
        percentage_of_calories = (calories_from_fat/total_calories) * 100
        print(f"The percentage of calories that come from fat is: {percentage_of_calories:.2f}%.")
        if percentage_of_calories < 30:
            print("The food is low in fat.")
calculate_calories_of_fat()


