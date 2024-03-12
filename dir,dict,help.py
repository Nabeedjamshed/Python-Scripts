# ye teeno object introspection krne ke lie use krte hai. Object introspection means aap dekhna chate ho ke us object mai kya kya mojood hai kis tanha se usse use kya ja skta hai


#*****dir()*******
#The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. 
#It is a useful tool for discovering what you can do with an object.

# x = [1,2,3]
# print(dir(x)) # dir show all occurences(method and attribute) present in class, list, tuple and many more.
# print(x.__add__)


#*****__dict__*******
# The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.

# class Person:
#     def __init__(self, name, age, version):
#         self.name = name
#         self.age = age
#         self.version = version
# p1 = Person("Nabeed",19,1)
# print(p1.__dict__) # Hr attribute or us ki value ko dictionary(key value pair) bta dega.


#*****help()*******
# The help() function is used to get help documentation for an object, including a description of its attributes and methods
print(help(str))