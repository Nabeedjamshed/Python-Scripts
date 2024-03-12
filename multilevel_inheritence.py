def greed(fx):
    def modify(self):
        print("Hello How are You?")
        fx(self)
        print("Thank You for using this function")
    return modify

class Human:
    def __init__(self, name, food, gender):
        self.name = name
        self.food = food
        self.gender = gender
    def show(self):
        print(f"Name: {self.name}",'\n'f"Food: {self.food}",'\n'f"Gender: {self.gender}")
class Employee(Human):
    def __init__(self, name,food, gender, id, workinghour):
        Human.__init__(self,name,food,gender)
        self.id = id
        self.workinghour = workinghour
    def salary(self):
        return 100 * self.workinghour
    # @greed
    def show(self):
        Human.show(self)
        print(f"Employee id: {self.id}",'\n'f"Working hour: {self.workinghour}")
        print(f"Salary: {self.salary()}")
class Programmer(Employee):
    def __init__(self, name,food,gender,id,workinghour,lang, ide):
        Employee.__init__(self,name,food,gender,id,workinghour)
        self.lang = lang
        self.ide = ide
    def salary(self):
        return 1000 * self.workinghour
    @greed
    def show(self):
        Employee.show(self)
        print(f"Programming Language: {self.lang}",'\n'f"IDE: {self.ide}")
        print(f"Salary: {self.salary()}")

print("Human Class")
h = Human("Sualiha","Burger","Female")
h.show()
print()
print("Employee Class")
e = Employee("Filza","Pizza","Female",120,20)
e.show()
print()
print("Programmer Class")
p = Programmer("Nabeed", "Biryani","Male",101,20,"C++","VS Code")
p.show()