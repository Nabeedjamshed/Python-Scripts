# Strings are immutable!!!
# st = input("Enter phase: ")
# print("the character of given phase is",len(st))
#
# x = st
# print(x.upper())
# print(x.lower())
# print(x.title())
#
# a = "!!!!!!Nabeed *******Nabeed !!!!!Nabeed"
# print(a.rstrip("*"))
# print(a.replace("Nabeed","Jamshaid"))
# print(a.split())
# b = "Nabeed is a good boy and he get 1st position!!!"
# print(len(b.center(80)))
# print(len(b))
# print(b.count("Nabeed"))
# print(b.endswith("!!!"))
# c = "Welcome to the console!!!"
# print(c.endswith("to",4,10)) #in python variables are over right
# print(c.find("to"))

x = "NABEED IS A GOOD BOY"
y = "              "
# print(x.find("llp"))
# print(x.index("ll"))

print(x.isalnum())
print(x.isalpha())
print(x.islower())
print(x.isprintable())
print(x)
print(y.isspace())
print(x.istitle())
print(x.isupper())
print(x.startswith("IS",7,9))
print(x.swapcase())

# f-strings!!!
letters = "Hey my name is {} and I am from {}"
name = 'Nabeed'
country = 'Pakistan'
print(letters.format(name,country))
print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")
print(f"{2 * 3}")

