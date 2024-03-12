# calls = int(input("Enter no of calls: "))
# if calls <= 100:
#     bill = 2000
# elif calls <= 150:
#     bill = 2000 + (calls - 100) * 0.60
# elif calls <= 200:
#     bill = 2050 + (calls - 150) * 0.50
# else:
#     bill = 2150 + (calls - 200) * 0.40
# print(f"Your monthly telephone bill is: {bill:.2f}")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print(f"Before swap: a = {a},b = {b}")
a, b = b, a
print(f"After swap: a = {a},b = {b}")

# def bubble_sort(l):
#     for i in range(0,len(l)-1):
#         for j in range(0,len(l)-i-1):
#             if l[i] > l[j] :
#                 temp = l[i+1]
#                 l[i+1] = l[i]
#                 l[i] = temp
#     return l
# lst = [26,3,11,21]
# print(bubble_sort(lst))

# name = input("Enter your name: ")
# print("Welcome",name)

# principle = int(input("Enter the value of principle: "))
# rate = int(input("Enter the value of rate: "))
# time = int(input("Enter the value of time: "))
# simple_interest = (principle * rate * time) / 100
# print(f"The simple interest is: {simple_interest} rupees")

# calls = int(input("Enter the number of calls: "))
#
# if calls <= 100:
#     bill = 2000
# elif calls <= 150:
#     bill = 2000 + (calls - 100) * 0.60
# elif calls <= 200:
#     bill = 2050 + (calls - 150) * 0.50
# else:
#     bill = 2150 + (calls - 200) * 0.40
#
# print(f"Your monthly telephone bill is Rs. {bill:.2f}")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print(f"Before swapping: a = {a}, b = {b}")

a, b = b, a

print(f"After swapping: a = {a}, b = {b}")