# for j in range(-4):
#     for i in range(1,j+1):
#         print("*",end="")
#     print()
#
# for i in range(10):
#     for j in range(1,i+1):
#         print('*',end="")
#     print()
# for i in range(9):
#     for j in range(9,i+1,-1):
#         print('*',end="")
#     print()

# for i in range(10):
#     for j in range(1,9-i):
#         print('*',end="")
#     print()
# (b)
# i = 1
# while i <= 8:
#     print("*" * i)
#     i += 1
# # (c)
# i = 8
# while i >= 1:
#     print("*" * i)
#     i -= 1

# num = 1
# while num <= 100:
#     if num % 2 != 0:
#         print(num,end=" ")
#     num += 2

def factorial(n):
    result = 1
    while n > 0:
        result = result * n
        n -= 1
    return result
i = 0
while i <= 10:
    print(f"The factorial of {i} is {factorial(i)}")
    i = i + 1

# (b)
# i = 1
# while i <= 8:
#     print("*" * i)
#     i += 1
# # (c)
# i = 8
# while i >= 1:
#     print("*" * i)
#     i -= 1
# (a)
# i = 1
# while i <=4:
#     print("*" * 14)
#     i += 1
# while i <= 8:
#     print(" " * 14 + "*" * 14)
#     i += 1