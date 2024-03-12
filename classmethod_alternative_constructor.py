# However, there are times when you may want to create an object in a different way, or with different initial values, 
# than what is provided by the default constructor(means default constructor __init__ mai jo arg die hai unhe different ways se derhe tu ek alternatibe constructor bna lete ke agr default constructor ke arg ke mutabiq values na milain tu wo alternative constructor ko use krle). 
# This is where class methods can be used as alternative constructors.



# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     @classmethod
#     def new(cls, string): # isse alternative constructor islie keh rhe ke agr data us format mai nhi aaya jo init mai hai tu us ke bager ye run hoga islie isse alternative constructor krh rhe.
#         return cls((string.split("-")[0]), int(string.split("-")[1]))

# e1 = Employee("Nabeed",120000)
# print(e1.name)
# print(e1.salary)

# string = "Nabeed-120000"
# e2 = Employee.new(string)
# print(e2.name)
# print(e2.salary)





# Another common use case for class methods as alternative constructors is when you want to create an object with a different set of 
# default values than what is provided by the default constructor. For example, consider a class named "Rectangle" that has two attributes:
# "width" and "height". The default constructor for the class might look like this:

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height


# # But what if you want to create a Rectangle object with a default width of 10 and a default height of 5? You can define a class method 
# # named "square" to do this:

# class Rectangle:
#   def __init__(self, width, height):
#     self.width = width
#     self.height = height
#     print(f"Height is {self.height}, and Width is {self.width}")
#   @classmethod
#   def square(cls, size):
#     return cls(size, size)


# # Now you can create a square rectangle like this:
# rectangle = Rectangle.square(10) # default value 10 set krdega ye bydefault width and height 10 set krdega




# rec = Rectangle(12,12)


class Bank:
    def __init__(self, principle, interestrate, year):
        self.principle = principle
        self.interestrate = interestrate
        self.year = year
        self.returnvalue = self.principle
        self.i = 0
        while self.i < self.year: 
            self.returnvalue = self.returnvalue * (1 + self.interestrate)
            self.i += 1
    
    @classmethod
    def new(cls, principle, interestrate, year):
        interestrate = float(interestrate) / 100
        return cls(principle, interestrate, year)
    def show(self):
        print(f"Principle amount is: {self.principle}, interest rate value is {self.interestrate} and after {self.year} year return value is {self.returnvalue}")
p = int(input("Enter the principle amount: "))
r = float(input("Enter the interest rate: "))
y = int(input("Enter the year: "))

b1 = Bank(p,r,y)
b1.show()

p1 = int(input("Enter the principle amount: "))
r1 = int(input("Enter the interest rate: "))
y1 = int(input("Enter the year: "))


b2 = Bank.new(p1,r1,y1)
b2.show()


