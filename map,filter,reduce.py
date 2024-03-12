# #****Lambda****
# x = int(input("Enter the number: "))
# y = lambda x:x*x*x # argument:return value
# print(y(x))

# #*****MAP*******
# l = [2,3,4,6,8,9]
# def cube(x):
#     return x*x*x
# print(list(map(cube,l)))
# print(list(map(lambda x:x*x*x,l))) # ---> list map or lambda function ko list mai convert krdega like(0x00000188943104A0> -----> readable value)
# print(list(map(lambda x:x%2==0,l))) # --> in map this statements returns a boolean list jis per ye condition T hogi list mai wha True ajaega otherwise False. [True, False, True, True, True, False]

# #*******Filter*******
# l = [2,3,4,6,8,9]
# def new(a):
#     return a>4
# print(list(filter(new, l)))   # ---> list ki hr value ke lie filter function ya tu True ya False return krega jin ke lie ye True hoga wo values print hojaengi.
# print(list(filter(lambda a:a>4, l)))
# print(list(filter(lambda a:a%2==0, l))) #---> return even numbers

#***Reduce****
# from functools import reduce
# l = [2,3,4,6,8,9]

# Solution how to reduce function works
# l = [5,4,6,8,9]
# l = [9,6,8,9]
# l = [15,8,9]
# l = [23,9]
# l = [32] ---> this value is shown in output

# print(reduce(lambda x, y:x+y, l)) # ---> provide sum of whole list by reducind technique


# Map, Filter and Reduce:
# In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence.
# These functions are known as higher-order functions, as they take other functions as arguments.

# map
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. 
# The map function has the following syntax:
# map(function, iterable)

# filter
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns 
#a new sequence containing only the elements that meet the predicate. The filter function has the following syntax:
# filter(predicate, iterable)

# The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. 
#The iterable argument can be a list, tuple, or any other iterable object.

# reduce
# The reduce function is a higher-order function that applies a function to a sequence and returns a single value. 
#It is a part of the functools module in Python and has the following syntax:
# reduce(function, iterable)

# The function argument is a function that takes in two arguments and returns a single value. 
#The iterable argument is a sequence of elements, such as a list or tuple.

# The reduce function applies the function to the first two elements in the iterable and then applies 
#the function to the result and the next element, and so on. The reduce function returns the final result.