def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(10))

# n = int(input("Enter No: "))
# if n%2 != 0:
#     print("Weird")
# elif n%2 == 0 and n>=2 and n<=5:
#     print("Not Weird")
# elif n%2 == 0 and n>=6 and n<=20:
#     print("Weird")
# elif n%2 == 0 and n>20:
#     print("Not Weird")

# a = float(input(""))
# b = float(input(""))
# print("0")
# print(a/b)

# n = int(input(""))
# for i in range:
#     print(n**2)


