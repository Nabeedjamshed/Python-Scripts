import math
s = float(input("Enter height (in ft): "))
g = 32
u = float(input("Enter initial velocity (in ft/sec): "))
v = math.sqrt((2*g*s)+(u**2))
print("The final velocity of stone is",v,"ft/sec")
# initial velocity of stone is zero because stone is at rest before dropped