# class Employee:
#     name = 'Nabeed'
#     occupation = 'Software Developer'  # ---> this are default values baat mai inko change krskte.
#     networth = 1000000000
#     def info(self): # self means wo object jiske lie ye method call kya jarha hai.jese ye method agr (a) ke lie call horha tu self.name means (a) ka name
#         print(f"{self.name} is a {self.occupation}.")

# a = Employee()
# b = Employee()
# c = Employee()
# a.name = "Filza" # ---> to change the name of an object
# a.occupation = 'Accounter'
# b.name = "Sualiha"
# b.occupation = "AI Engineer"
# # print(a.name("Filza"))
# # print(a.occupation)
# # print(a.networth)
# a.info()
# b.info()
# c.info() # --> agr c ki koi value nhi dain tu default values c mai aajaengi
import math as m

class Point:
    def __init__(self,x, y):
        self.a = x
        self.b = y
    def printdata(self):
        print(f"Your point is: ({self.a},{self.b})")
class Calculator:
    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2
    def distance(self):
        diff1 = (self.o2.a - self.o1.a)
        diff2 = (self.o2.b - self.o1.b)
        sq1 = pow(diff1, 2)
        sq2 = pow(diff2, 2)
        add = sq1 + sq2
        sr = m.sqrt(add)
        print("The distance between two points is: ",sr)

x1 = int(input("Enter the value of X1: "))
y1 = int(input("Enter the value of Y1: "))
p = Point(x1, y1)
p.printdata()

x2 = int(input("Enter the value of X2: "))
y2 = int(input("Enter the value of Y2: "))
q = Point(x2,y2)
q.printdata()

cal = Calculator(p,q)
cal.distance()

       
