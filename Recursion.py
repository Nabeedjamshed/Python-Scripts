# Recursion means function mai function ko call krna like factorial ka function bna kr us mai factorial ko hi call krdya
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(5))
print(factorial(9))
print(factorial(7))