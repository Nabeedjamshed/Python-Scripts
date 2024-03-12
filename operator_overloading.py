class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self, x): # This is v1.__add__(v2) and x is this case is a v2 and self is a v1
        print("Addition")
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
    def __sub__(self, x):
        print("Subtraction")
        return Vector(self.i - x.i, self.j - x.j, self.k - x.k)
    def __mul__(self, x):
        print("Multiplication")
        return Vector(self.i * x.i, self.j * x.j, self.k * x.k)
    def __truediv__(self,x):
        print("Division")
        return Vector(self.i / x.i, self.j / x.j, self.k / x.k)
    def __lt__(self,x):
        print("Less than")
        return Vector(self.i < x.i, self.j < x.j, self.k < x.k)
    def __gt__(self,x):
        print("Greater than")
        return Vector(self.i > x.i, self.j > x.j, self.k > x.k)
    def __eq__(self,x):
        print("Equal to")
        return Vector(self.i == x.i, self.j == x.j, self.k == x.k)
v1 = Vector(4,9,10)
print(v1)
v2 = Vector(2,3,2)
print(v2)
print(v1+v2)
print(v1-v2)
print(v1*v2)
print(v1/v2)
print(v1<v2)
print(v1>v2)
print(v1==v2)


# Operator overloading is a feature in object-oriented programming languages that allows developers to redefine the behavior of certain operators 
# (like +, -, *, /, etc.) for custom classes. This means that operators can be made to work differently depending on the types of operands involved.