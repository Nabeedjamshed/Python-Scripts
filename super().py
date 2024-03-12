# class Parent:
#     def parent_method(self):
#         print("This is a parent method")
# class Child(Parent):
#     def __init__(self):
#         print("This is a child method")
#         # super().parent_method() # agr a.parent_method() likenge tu wo us attribute ke lie just run hoga but age super keyword use krke usse child 
#         # class mai hi dal dain tu jb bhi child ka object bnega wo parent ka method uske lie run hojaega.
# a = Child()
# a.parent_method()


# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
# class Programmer(Employee):
#     def __init__(self,name,id,lang):
#         super().__init__(name,id)  # Parent ka constructor super keyword se call krlya tu again name and id ka attribute bnane ki need nhi hai.
#         self.lang = lang

# emp = Employee("Nabeed",234)
# print(emp.name)
# print(emp.id)

# pg = Programmer("Rohan", 432, "Python")
# print(pg.name)
# print(pg.id)
# print(pg.lang)


# class ParentClass1:
#     def parent_method(self):
#         print("This is the parent method of ParentClass1.")

# class ParentClass2:
#     def parent_method(self):
#         print("This is the parent method of ParentClass2.")

# class ChildClass(ParentClass1, ParentClass2):
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()  # This call first parent_method

# child_object = ChildClass()
# child_object.child_method()


class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")

class ParentClass2:
    def parent_method(self):
        print("This is the parent method of ParentClass2.")

class ChildClass(ParentClass1, ParentClass2):
    def parent_method(self):
        print("Nabeed")
        super().parent_method()
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()  # agr child mai parent method bnaya hai or usse call krenge tu wo print hoga or us ke baad agr super keyword dya hai tu parent class1 print hogi.