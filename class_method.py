# class Employee:
#     company = "Apple"
#     def show(self):
#         print(f"The name of the Employee is {self.name} and company is {self.company}")

#     @classmethod # --> Jb ye likh dya tu ab ye class method bn gya hai means yha whole class access horhi hai tu ab self nhi cls dena hai before decorator yha kuch bhi likh skte the like self ki jga tinde aalo sb likh skte the.Decorator lgane se bs ye howa hai ke hum class ka variable change kr pae emp1 ke nhi jo Apple ko Tesla kya tha wo just us instance ke lie change howa tha class variable is not change but jb decorator lga kr change kya tu variable change hogya bcz us ne whole class hi us method mai access kradi
#     def changecom(cls, newcom):
#         cls.company = newcom
# emp1 = Employee()
# emp1.name = "Nabeed"
# emp1.show()
# emp1.changecom("Tesla")
# emp1.show()
# # print(Employee.company) # ---> Output: Apple. it means class variable is not change
# print(Employee.company) # ---> Output: Tesla. due to @classmethod it shows Tesla means class variable change hogya kyu ke is decorator se changecom method main whole class access hogae tu ab class ke variable change krskte.


# class Employee:
#     def nam(self,name): # Jha self likha hai yha necessary nhi hai ke self hi likhain yha tinde aalo sb likh skte koi error nhi aaega yha bs isse ek arg chaeye jha object aajae jiske lie ye method run horha.
#         self.name = name
#     def show(self):
#         print(f"NAME: {self.name}")
# e1 = Employee()
# e1.nam("Nabeed")
# e1.show()