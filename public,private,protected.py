# PUBLIC
# class Employee:
#     def __init__(self):
#         self.name = "Nabeed"
# a = Employee()
# print(a.name)

#PRIVATE
class Employee:
    def __init__(self):
        self.__name = "Nabeed" # '__' makes variable and method private but ye weak indicator hai isko access krskta object with some technique
a = Employee()
# print(a.__name) # This shows an error
print(a._Employee__name) # This doesnot show an error (is technique ne aap private attribute and method ko access krskte is lie (__) se bnne 
#                          wale private member ko kehte hai ke ye weak hai you can access this.It means agr private bna dya hai tu directly 
#                          tu access nhi krskte but indirectly access krskte hai.
# (a._Employee__name) This is called name mangling.Name mangling mai jo private attribute hai(__name) uska name badl ke rakh dya jata hai

print(a.__dir__()) #---> __dir__() method se ye check krskte ke us object per kon konse attribute or method run kie jaskte hai.