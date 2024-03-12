# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def show(self):
#         print(f"The Employee name is {self.name} and his id is {self.id}")
# class Programmer(Employee):
#     def lang(self,language):
#         self.language = language
#         print(f"The language that he is used in his code is: {self.language}")
# e1 = Employee("Nabeed",101)
# e1.show()
# e2 = Programmer("Talha",102)
# e2.show()
# e2.lang("C++")

class GrandFather:
    def __init__(self, name, age, occ):
        self.name = name
        self.age = age
        self.occ = occ
    def show(self):
        print(f"Name is: {self.name} ",'\n'
              f"Age is: {self.age} ",'\n'
              f"Occupation is: {self.occ} ")


class Father(GrandFather):
    def car_app(self, car,apprt):
        self.car = car
        self.appartment = apprt
        print(f"Car: {self.car}",'\n'
              f"Appartment: {self.appartment}")
        

class Son(Father):
    def personal(self,lang,habit):
        self.lang = lang
        self.habit = habit
        print(f"Habit is: {self.habit}",'\n'
              f"The language that he is used in his code is: {self.lang}")
        
gn = input("Enter the GrandFather's Name: ")  
ga = int(input("Enter the GrandFather's Age: ")) 
go = input("Enter the GrandFather's Occupation: ") 
      
p = input("Enter the Father's Name: ")  
q = int(input("Enter the Father's Age: ")) 
r = input("Enter the Father's Occupation: ")
s = input("Enter the Father's Car Name: ")
t = input("Enter the Father's Appartment Name: ")

sn = input("Enter the Son's Name: ")  
sa = int(input("Enter the Son's Age: ")) 
so = input("Enter the Son's Occupation: ")
sc = input("Enter the Son's Car Name: ")
st = input("Enter the Son's Appartment Name: ")
scl = input("Enter the Programming Language Name: ")
sh = input("Enter the Son's Habit: ")

print('\n')
obj1 = GrandFather(gn,ga,go)
obj1.show()
print('\n')

obj2 = Father(p,q,r)
obj2.show()
obj2.car_app(s,t)
print('\n')

obj3 = Son(sn,sa,so)
obj3.show()
obj3.car_app(sc,st)
obj3.personal(scl,sh)
print('\n')