class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(self.radius,self.radius)
    def area(self):
        return 3.14 * super().area()


s = Shape(3,4)
print(s.area())
c = Circle(5)
print(c.area())

class Workers:
    companyname = "Apple"
    def __init__(self, name, wkhour):
        self.name = name
        self.workinghour = wkhour
    def show(self):
        print(f"{self.name} salary is: ")

    def salary(self):
        return 100 * self.workinghour
class Managers(Workers):
    def __init__(self, name, wkhour):
        super().__init__(name,wkhour)
    def salary(self):
        return 100 * super().salary()
    
w = Workers("Rohan",20) 
w.show()
print(w.salary())

m = Managers("Nabeed",10)
m.show()
print(m.salary())

# It's important to note that when you override a method, the new implementation must have the same method signature as the original method. 
# This means that the number and type of arguments, as well as the return type, must be the same.

# class Shape:
#     def area(self,x,y):
#         print("Calculate area")
#         self.x = x
#         self.y = y
#         print(self.x * self.y)
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         print("Calculating area of a circle...")
#         super().area(3,4)
#         return 3.14 * self.radius * self.radius
# c =Circle(5)
# print(c.area())



    


