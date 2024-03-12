class Employee:
    company_name = "Apple"
    noofemployee = 0
    def __init__(self,name):
        self.name = name   # instance variable bcz hr instance(object) isse apne lie use krskta
        self.raise_amt = 0.2
        Employee.noofemployee += 1 # this is class variable yha self.noofemployee nhi likhna wrna hr object ke lie ye self run hoga tu sb ka 1 hi show hoga kyu ke ek object ke lie ye 0 to 1 hoga tu jb dosra object aaega tu uske lie bhi 0 to 1 hi hoga bcz self likha hai is lie Employee class ka name likhenge ke class jitni baar use ho ye increment hojae.
    def show(self):
        print(f"The name of the Employee is {self.name} his employee number is {self.noofemployee} and his raise amount is {self.raise_amt} and the company name is {self.company_name}")

# Employee.show(emp1) ---> line 8 and 10 have same work
emp1 = Employee("Nabeed")
# emp1.noofemployee = 3  # ye bhi krskte
emp1.show() 

emp2 = Employee("Filza")
emp2.raise_amt = 0.5 # instance variable ko aese change bhi krskte
emp2.company_name = "Google" # class variable ko bhi change krskte first compiler ye check krega ke in object ka koi instance variable hai agr hai tu usse print krae ga agr nhi hai tu class variable ko print kra dega class variable jitne bhi object us class ke lie bne hai un sb ke lie same hota object apne lie usse change krskta hai like Filza ne apna class variable change krdya.
emp2.show()


# Instance Variables
# Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represents an employee.