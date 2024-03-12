# It's important to note that, in case of multiple inheritance, Python follows a method resolution order (MRO) to resolve conflicts between methods or 
# attributes from different parent classes. The MRO determines the order in which parent classes are searched for attributes and methods

def morn(fx):
    def modify(self):    
        print("Good Morning")
        fx(self)
        print("Thank You")
    return modify
class GrandFather:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def printinfo(self):
        print("Hello GrandFather")
class Father:
    def __init__(self, property, hobbies):
        self.property = property
        self.hobbies = hobbies
    def printinfo(self):
        print("Hello Father")
class Son(GrandFather,Father):
    def __init__(self,name,age,salary,property,hobbies,lang,nature):
        GrandFather.__init__(self,name,age,salary)
        Father.__init__(self,property, hobbies)
        self.lang = lang
        self.nature = nature
    # def printinfo(self):
    #     print("Hello S")
    @morn
    def show(self):
        print(f"Name: {self.name}",'\n'f"Age: {self.age}",'\n'f"Salary: {self.salary}",'\n'f"Property: {self.property}",'\n'f"Hobbies: {self.hobbies}",'\n'f"Programming Language: {self.lang}",'\n'f"Nature: {self.nature}")
        self.printinfo() # printinfo ko yha call krdya ab agr in class mai printinfo hoga tu wo print hojaega otherwise upper ki classes ka print hoga jo phele likha hoga.self inlie lgaya bcz jis object ke lie ye method run horha wo object yha aaega.

s = Son("Nabeed",19,120000,"In USA","Programming","C++","Peace")
s.show()
# s.printinfo() # print() method agr isse Son mai nhi milega tu wo inherit class mai dekhega or un mai agr dono mai same method hai tu jo class ka name phele likha hai us ka method print kradega like Son(GrandFather, Father) mai GF ka method print hoga.

# print(Son.mro()) # age method ya attribute conflict krte hai classes mai tu mro() method se order dekh skte ke phele compiler kis class ke method ko dekhega