# def term():
#     a = float(input("Enter first term: "))
#     d = float(input("Enter common difference: "))
#     n = float(input("Enter the term which you want to calculate: "))
#     tn = a+(n-1)*d
#     if n < 1:
#         print("Sorry, you enter invalid input")
#     else:
#         print("The",n,"th","term is",tn)
#     term()
#     condition = input("Do you wants to calculate more terms. Say 'yes' or 'no'")
#     while condition == 'yes':
#      term()
#      condition = input("Do you wants to calculate more terms. Say 'yes' or 'no'")
#     else:
#         print("Thank You \'Have a Good Day\'")

# name = input("Enter your name: ".title())
# f_name = input("Enter your father name: ".title())
# roll_no = int(input("Enter your roll number: "))
# sub1 = input("Enter subject name: ".title())
# marks1 = int(input("Enter obtained marks: ".title()))
# sub2 = input("Enter subject name: ".title())
# marks2 = int(input("Enter obtained marks: ".title()))
# sub3 = input("Enter subject name: ".title())
# marks3 = int(input("Enter obtained marks: ".title()))
# sub4 = input("Enter subject name: ".title())
# marks4 = int(input("Enter obtained marks: ".title()))
# sub5 = input("Enter subject name: ".title())
# marks5 = int(input("Enter obtained marks: ".title()))
# obtained_marks = marks1+marks2+marks3+marks4+marks5
# percentage = (obtained_marks/500)*100
# print("\nName: ",name,"\nFather Name: ",f_name,"\nRoll No.",roll_no,"\nSubjects \t Marks Out of 100")
# print(sub1.title(),"\t\t",marks1)
# print(sub2.title(),"\t",marks2)
# print(sub3.title(),"\t",marks3)
# print(sub4.title(),"\t",marks4)
# print(sub5.title(),"\t\t",marks5)
# print("Total Marks : 500")
# print("Obtained Marks : ",obtained_marks)
# print("Percentage : %.2f"%percentage)
# if(percentage >= 87 and percentage <= 100):
#     print(name,"HAS OBTAINED A GRADE")
#
# elif(percentage >= 75 and percentage <= 86):
#     print(name,"HAS OBTAINED B GRADE")
#
# elif(percentage >= 65 and percentage <= 74):
#         print(name, "HAS OBTAINED C GRADE")
#
# elif(percentage >= 55 and percentage <= 64):
#     print(name,"HAS OBTAINED D GRADE")
# elif(percentage >= 0 and percentage <= 54):
#     print(name,"SORRY YOU ARE FAIL")
# else:
#     print("PLEASE ENTER CORRECT INFORMATION")
# #
# initial = int(input("Enter initial value: ".title()))
# final = int(input("Enter final value: ".title()))
# for j in range(initial,final+1):
#     for i in range(initial,final+1):
#         print(j*i,end="\t")
#     print()

# a = float(input("Enter the value of a: "))
# b = float(input("Enter the value of b: "))
# c = float(input("Enter the value of c: "))
# if a == 0:
#     print("the equation cannot solve as there is a zero division")
# else:
#     w = b ** 2
#     s = 4*a*c
#     if w > s:
#         import math
#         x = math.sqrt(w - s)
#         y1 = (-b + x) / (2 * a)
#         y2 = (-b - x) / (2 * a)
#         print("The Ans of The Quadratic Eq is", y1, "and", y2)
#         round(y1.real, 2)
#         round(y2.real, 2)
#     else:
#         import cmath
#         x = cmath.sqrt(w - s)
#         y3 = (-b + x) / (2 * a)
#         y4 = (-b - x) / (2 * a)
#         print("The Ans of The Quadratic Eq is",y3,"and",y4)
#         round(y3.real, 2)
#         round(y4.real, 2)

# def term():
#     a = float(input("Enter first term: "))
#     d = float(input("Enter common difference: "))
#     n = float(input("Enter the term which you want to calculate: "))
#     tn = a+(n-1)*d
#     if n < 1:
#         print("Sorry, you enter invalid input")
#     else:
#         print("The",n,"th","term is",tn)
# term()
# condition = input("Do you wants to calculate more terms. Say 'yes' or 'no'")
# while condition == 'yes':
#  term()
#  condition = input("Do you wants to calculate more terms. Say 'yes' or 'no'")
# else:
#      print("Thank You \'Have a Good Day\'")

# def palindrone(word):
#     a = word.casefold()
#     b = word.join(reversed(a))
#     return b
# wrd = input("Enter The World: ").casefold()
# x = palindrone(wrd)
# if x == wrd:
#     print("Yes \'Your String is Palindrone\'")
# else:
#     print("Sorry \'Your String isn't Palindrone\'")

# matrix1 = [[1,2,3],
#            [4,5,6],
#            [7,8,3]]
# matrix2 = [[5,5,2],
#            [5,1,3],
#            [1,1,6]]
# matrix3 = [[0,0,0],
#            [0,0,0],
#            [0,0,0]]
# for i in range(len(matrix1)):
#     for j in range(len(matrix1[0])):
#         matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
# for k in matrix3:
#     print(k)

# matrix1 = [[1,2,3],
#            [4,5,6],
#            [7,8,3]]
# matrix2 = [[5,5,2],
#            [5,1,3],
#            [1,1,6]]
# matrix3 = [[0,0,0],
#            [0,0,0],
#            [0,0,0]]
# for i in range(len(matrix1)):
#     for j in range(len(matrix2[0])):
#         for k in range(len(matrix2)):
#             matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
# for i in matrix3:
#     print(i)

a = input("Enter the String: ")
b = a[-1::-1]
if a == b:
    print("Yes \'Your String is Palindrone\'")
else:
    print("Sorry \'Your String isn't Palindrone\'")


# Access single value
# dic = {'name': 'Nabeed', 'age': '19', 'profession': 'software engineer'}
# print(dic['name'])
# print(dic.get('profession'))
#
# # Access multiple value
# print(dic.values())
# print(dic.keys())
# print(dic.items())
# for keys in dic:
#     print(keys)
# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)
# print(info.keys())
# print(info.values())
#
# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")


info = {'name': 'Nabeed', 'age': 19, 'profession': 'software engineer'}
# for key in info.keys():
#     print(f"The value correspond to the key {key} is {info[key]}")
for key, value in info.items():
  print(f"The value correspond to the {key} is {value}")