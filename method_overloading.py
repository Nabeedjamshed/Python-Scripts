class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

s = Shape(3,4)
print(s.area())
c = Circle(5)
print(c.area())


# Method overloading refers to defining multiple methods in a class with the same name but with different parameters
#  or arguments. In Python, method overloading is not directly supported as in some other programming languages like
#  Java or C++, where you can have multiple methods with the same name but different parameters.