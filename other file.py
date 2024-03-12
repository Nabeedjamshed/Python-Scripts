# number = 12
# string = "4"
# number_string = int(string)
# sum = number + number_string
# print("THE SUM IS",sum)
#
# a = 5
# print(type(a))
# b = 8.8
# print(type(b))
# c = a + b
# print(c)
# print(type(c))

# x = input("ENTER FIRST NUMBER: ")
# y = input("ENTER SECOND NUMBER: ")
# print("THE ANS IS",int(x) // int(y))

name = "nabeed"
# to concotinate two string by using \ or by using single code ''
apple = "he said, \" i am very handsome"
mango = 'he said, "you are beauty'
print(apple)
print(mango)
# to use multiple line string so use triple single codes or double code
st = """Most respectfully I beg to say that I want to apply for the position of : 
Kindly consider my application and do the needful."""
print(st)

# indexing
name = "NABEED" # string is a sequence of character and indexing means
# nabeed mai konsa word kis jga per hai like 0,1,2,3,4 tu ye bta dega eg:
# most of the programming language main indexing 0 se start hoti hai
print(name[0])
print(name[5])
# for loops
for character in st:
    print(character)
# python string is just like ary of characters while ary means collection of items

fruit1 = "Mango"
fruit2 = "Orange"
len1 = len(fruit1)
len2 = len(fruit2)
print("Mango contains",len1,"letters in eng language.")
print("Orange contains",len2,"letters in eng language.")
print(fruit1[1:3])
print(fruit2[0:-1]) # [] use for slicing
print(fruit1[:])
print(len(fruit1))
print(fruit1[0:-3])
print(fruit1[:len(fruit1)-3])
print(fruit1[-3:-1])
nm = "HARRY"
print(nm[-4:-2])

# rstrip removes backword strip not forward
a = "******Nabeed******"
print(a.rstrip("*"))

# replace means change old string into new string
b = "Harry"
print(b.replace("Harry","Nabeed"))

# using split() we can make list
c = "NABEED !!!!!!! JAMSHAID"
print(c.split( ))

# class average
x = int(input("ENTER TOTAL NO OF STUDENTS:"))
sum = 0
for i in range(1,x+1):
    marks = int(input("ENTER MARKS:"))
    sum = sum + marks
avg = sum/x
print("THE CLASS AVG IS",avg)

# for j in range(5):
#  for i in range(5):
#      print(i,end = " ")
#  print()

# x = "HELLO WORlD"
# lenght = len(x)
# print("ANS IS",lenght)

y = abs(-2.5)
print(y)
#indexing
s = "HELLO WORLD"
z = s[-9:-5]
print(z)