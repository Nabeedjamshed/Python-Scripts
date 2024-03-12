centigrade_temp=float(input("ENTER TEMP IN DEGREE CENTIGRADE : "))
print("THE TEMP IN FAHRENHEIT IS : ",(centigrade_temp*9/5)+32)

fahrenheit_temp = float(input("ENTER TEMP IN DEGREE FAHRENHEIT : "))
print("THE TEMP IN CELSIUS IS : " , (fahrenheit_temp-32)*5/9)

length = float(input("ENTER LENGTH OF A RECTANGLE IN m : "))
breadth = float(input("ENTER BREADTH OF A RECTANGLE IN m : "))
area = length*breadth
print("THE AREA OF A RECTANGLE",length,"and",breadth,"is",area,"m\u00b2.")

from math import pi
radius = float(input("ENTER RADIUS OF A SPHERE : "))
volume = (4 / 3) * pi * (radius ** 3)
print("VOLUME OF A SPHERE IS : %.2f" %volume,"m\u00b3")

x = input("ENTER YOUR NAME : ")
print("NAME IN UPPER CASE : ",x.upper())
print("NAME IN LOWER CASE : ",x.lower())
print("NAME IN TITLE CASE : ",x.title())