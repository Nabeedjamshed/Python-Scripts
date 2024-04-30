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

# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# print(f"Before swap: a = {a},b = {b}")
# a, b = b, a
# print(f"After swap: a = {a},b = {b}")

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

# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))

# print(f"Before swapping: a = {a}, b = {b}")

# a, b = b, a

# print(f"After swapping: a = {a}, b = {b}")

# n = input("Enter your name: ")
# if n == 'Nabeed':
#     print('😊')
# else:
#     print('😂')

amount = int(input("Enter amount in rupees: "))
l = [1000,500,100,50,10,5,2,1]
# new = []
# div = amount % l[0]
# new.append(div)
# i = 0
# x = new[i] % l[i+1]
# i += 1
# print(new)
# for i in l:

new = amount % l[0]
new1 = new % l[1]
new2 = new1 % l[2]
new3 = new2 % l[3]
new4 = new3 % l[4]
new5 = new4 % l[5]
new6 = new5 % l[6]
new7 = new6 % l[7]
print(new)
print(new1)
print(new2)
print(new3)
print(new4)
print(new5)
print(new6)
print(new7)
