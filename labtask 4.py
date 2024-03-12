# Programming Fundamental Lab Task 4 "NABEED ALI" FESE SEC :

# Q:4 Write a program to calculate the volume of a sphere.

from math import pi

radius = float(input("ENTER RADIUS OF A SPHERE : "))

volume = (4 / 3) * pi * (radius ** 3)

print("VOLUME OF A SPHERE IS : %.2f" %volume,"m\u00b3")