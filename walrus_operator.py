# The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. 
# This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.

# a = False
# print(a)
# print(a := True)

# foods = []
# while True:
#     n = input("Enter the name of food: ")
#     if food == "quite":
#         break
#     foods.append(n)
# print(foods)
# foods = []
# while(n := input("Enter the name of food: ")) != "quite":
#     foods.append(n)
# print(foods) 


# l = [1,2,3,4,5]
# while(n := len(l)) > 0:
#     l.pop()
#     print(l)

names = ['Nabeed', 'Filza', 'Sualiha']
if (name := input("Enter the names: ")) in names:
    print(f"Hello {name}")
else:
    print("Not found")