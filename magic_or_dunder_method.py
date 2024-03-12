from emp import Employee # ---> emp name ki file mai Employee name ki class bnae hoe hai usse import krrhe hai tu us class ka hr method is file mai import
#                               hojaega this is best for encapsulation bcz aap ki poori class encapsule hoe wi hai in main file wo hidden hai us mai aap ne kya kya method define kie hai 
#                               user ko nhi pta wo just usse use krrha hai. 

e = Employee("Nabeed")
print(e) # no need to write str bcz in class __str__ method likha hoe or ye object ka attribute usse paas horha tu without str bhi print hojaega shi output.
print(repr(e)) # if you want ke __repr__ mai jo likha hai wo yha print ho tu repr likhna hai wrna by default wo jo __str__ mai likha hai whi print kradega.
#                repr islie hota ke object fall back krjata hai mtlab agr main class mai isse __str__ method nhi dikega tu ye jo __repr__ mai likha hai wo print kradega. 
#                repr ek method hota hai jo represent krta hai object keus tariqe ko jis se is object ko recreate kya ja skta hai means agr str nhi mila tu object repr lekr
#                create hojaega or agr object phele se str se create hai or repr de kr object ko call krain tu ooject recreate hojaega.yha repr ka name likha hai usse call nhi kya phr bhi us ki value print hogae.
print(len(e)) # agr just len likhte tu error aata wo bolta ke in class koi len method define nhi hai ytu is lie phele class mai __len__ length ka dunder method define krna parhega.
e() # object ko jb as a function run krna chaenge tu ye __call__ method class mai dhondega or agr isse milega tu us mai jo likha hai wo apne lie 
#   print kradega means agr object mai name hai like Nabeed or call method mai self.name likha howa hai tu Nabeed print hojaega. in short __call__ 
#   mai jo likha hoga wo print kradega.

    
# class Math:
#     def __init__(self, number):
#         self.number = number+1
#     def __call__(self):
#         def fabonacci(self):
#             if self == 0:
#                 return 0
#             elif self == 1:
#                 return 1
#             else:
#                 return fabonacci(self - 2) + fabonacci(self - 1)
#         for self.i in range(self.number):
#             print(fabonacci(self.i),end=' ')

# n = int(input("Enter the number: "))
# m = Math(n)
# m()
# print()
# n1 = int(input("Enter the number: "))
# m1 = Math(n1)
# m1()

# Dunder method jo in general likh kr call nhi krne hum ye nhi kehte print(__len__).len method ko tu call krte but isse nhi krte.