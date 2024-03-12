# class Myclass:
#     def __init__(self,num1):
#         self.num = num1
#     def addnum(self,num2):
#         self.num = self.num + num2
#     @staticmethod
#     def add(a,b): # --> Their is no mandatory to write self in method if you make a static method so ye self nhi leta.
#         #               Ye class ke instance se belong nhi krta isse just class ke name se bhi access krskte isse just 
#         #               class mai ship krdete hai ke agr ksi ko class dain jo is method ka faida utha skte. agr utility 
#         #               function bnana tu static method ko use krte hai. Utility function  is a type of function used in 
#         #               programming to perform a specific task or operation that is generally unrelated to the main purpose
#         #               of the program or the class in which it resides.
#         return a+b

# a = Myclass(3)
# print(a.num)
# a.addnum(4)
# print(a.num)
# print(a.add(2,3))
# print(Myclass.add(2,3)) # Staticmethod ko class ke name se bhi access krskte.



#Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator 
#and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods 
#are often used to create utility functions that don't need access to instance data.


class Math:
    @staticmethod
    def add(a, b):
        return a + b
result = Math()
print(result.add(1, 2)) # Output: 3


# In this example, the add method is a static method of the Math class. It takes two parameters a and b and returns their sum. The method can be called on 
# the class itself, without the need to create an instance of the class.
