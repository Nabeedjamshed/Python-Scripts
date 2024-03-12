# Parameterized Constructor in Python
class Employee:
    def __init__(self, n, o): # yha per self ki jga automatically a, b ajaenge jis waqt jis object ke lie ye run horha hoga wo object yha aajaega
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}.")
a = Employee("Nabeed", "Developer")
a.info()
b = Employee("Filza", "HR")
b.info()

# Constructor cannot return any value other than None


# Default Constructor in Python
class X:
    def __init__(self):
        print("Hello I am a student.")
    def printdata(self):
        print("Hello Nabeed")
x = X()
x.printdata()

# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.

# Example:
# class Details:
#   def __init__(self):
#     print("animal Crab belongs to Crustaceans group")
# obj1=Details()


# Output:
# animal Crab belongs to Crustaceans group