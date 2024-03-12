class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
class Person(Human): # This is single inheritence
    def __init__(self, name,age,address,occupation):
        Human.__init__(self,name,age)
        self.address = address
        self.occupation = occupation
    def show(self):
        print(f"Address: {self.address}")
        print(f"Occupation: {self.occupation}")
class Programmer(Human):
    def __init__(self, lang):
        self.lang = lang
    def show(self):
        print(f"Language: {self.lang}")
class Student(Person, Programmer): # This is multiple inheritence. So 2 inheritence aagae hai is lie ye hybrid inheritence hogae.
    def __init__(self, name,age,address,occupation,grade, classes,lang):
        Person.__init__(self,name,age,address,occupation)
        Programmer.__init__(self,lang)
        self.grade = grade
        self.classes = classes
    def show(self):
        Human.show(self)
        Person.show(self)
        Programmer.show(self)
        print(f"Grade: {self.grade}")
        print(f"Class: {self.classes}")

s = Student("Nabeed",19,"Karachi","Developer","A+","BESE","Python")
s.show()