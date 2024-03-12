# #decorators ek function hai jo dosre function ko lekr thora bhut update(modify/decorate) krdeta hai

# # *****Without Argument******
# def greed(fx):
#     def modify():
#         print("Good Morning")
#         fx() # --> this value print Hello World
#         print("Thanks for using this function")
#     return modify

# @greed  # ---> agr @dec nhi likhe tu greed(hello)() likhna parhega both have same work
# def hello():
#     print("Hello World")
# hello()


# # *****With Argument******
# def greed(fx):
#     def modify(*a,**b): #---> agr function mai argument dena hai tu yha btana parhega wrna argument paas hi nhi honge * shows tuple, ** shows dictionary(key and value pair). So, ye krne se jb good morning ke baad function run hoga tu wo arg lelega
#         print("Good Morning")
#         fx(*a, **b) # --> this value print Hello World
#         print("Thanks for using this function")
#     return modify

# @greed
# def hello(a,b):
#     print(a+b)
# hello(2,3)

# def dec(fx):
#     def modify(*a, **b):
#         print("Hello")
#         fx(*a, **b)
#         print("Thank You")
#     return modify

# @dec  
# def frd(a, b):
#     print(a+b)
# frd(3,4)
# dec(frd)(3,4)

# @dec
# def hello(a, b):
#     return a+b
# print(hello(2,3))  # --> not work in decorator show None