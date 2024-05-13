# import math as m
# import cmath as cm
# a = int(input('Enter the value of a: '))
# b = int(input('Enter the value of b: '))
# c = int(input('Enter the value of c: '))
# try:
#     sq_root = m.sqrt((b ** 2)-(4*a*c))
#     den = 2 * a
#     x = - b + sq_root / den
#     print('The answer is: ',x)
# except:
#     sq_root = cm.sqrt((b ** 2)-(4*a*c))
#     den = 2 * a
#     y = - b + sq_root / den
#     print('The answer is: ',y)
# import datetime
# mytime = datetime.datetime.now().date()
# print(mytime)
# mytime = datetime.datetime.now().time()
# print(mytime)

# for i in range(5):
#     for j in range(5):
#         print(j,end=' ')
#         # print(j,end=' ')
#     print()

# table_no = int(input("Enter the table no: "))
# table_limit = int(input("Enter the table limit: "))
# for i in range(1, table_limit+1):
#     print(f'{table_no} x {i} = {table_no * i}')

# no = int(input('Enter the number: '))
# fact = 1
# for i in range(1, no+1):
#     fact = fact * i
# print(fact)

# std = int(input("Enter total no. of students: "))
# sum = 0
# for i in range(1, std+1):
#     marks = int(input("Enter marks: "))
#     sum = sum + marks
#     avg = sum / std
# print("The class avg. is: ",avg)

# x = 'Nabeed'
# print(x.replace('Nabeed','Filza'))

# x = 'Nabeed !!!! Jamshed'
# print(x.split())

# s = input("Enter the string: ")
# vowels = 'aeiouAEIOU'
# vow = 0
# con = 0
# for i in s:
#     if i in vowels:
#         print(i,'is a vowel')
#         vow = vow + 1
#     else:
#         print(i,'is a consunent')
#         con = con + 1
# print("The total no. of vowel in phrase is: ",vow)
# print("The total no. of consunent in phrase is: ",con)

# mat1 = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# mat2 = [[1,4,3],
#         [2,5,7],
#         [7,8,6]]
# mat3 = [[0,0,0],
#         [0,0,0],
#         [0,0,0]]
# for i in range(len(mat1)):
#     for j in range(len(mat1[0])):
#         mat3[i][j] = mat1[i][j] + mat2[i][j]
# for k in mat3:
#     print(k)
# for i in range(len(mat1)):
#     for j in range(len(mat1[0])):
#         for k in range(len(mat3)):
#             mat3[i][j] += mat1[i][k] * mat2[k][j]
# for k in mat3:
#     print(k)

# for i in range(1, n+1):
#     fact = fact * i
# print(fact)
# n = int(input("Enter the number: "))
# fact = 1
# i = 1
# while i<=n:
#     fact = fact * i
#     i = i + 1
# print(fact)

# for i in range(5):
#     for j in range(5):
#         print(i,end=' ')
#     print()

# marks = []
# for i in range(3):
#     print(f'Data for {i}th rows!!')
#     for j in range(3):
#         m = int(input(f"Enter the marks of {j+1} student: "))
#         marks.append(m)
#         print()
# print(marks)

# for i in range(5):
#     for j in range(5):
#         if j == 2:
#             print(i,end=" ")
#         else:
#             print(j,end=' ')
#     print()
# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print(0,end=' ')
#         else:
#             print(j,end=" ")
#     print()

# def sum(a, b):
#     result = a + b
#     return result
# x = int(input("Enter the number 1: "))
# y = int(input("Enter the number 2: "))
# print(f"The sum of {x} and {y} is: {sum(x, y)}")

# def greed(name):
#     print(f'Hello {name}')
# greed('Nabeed')

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# x = int(input('Enter the no. : '))
# print(factorial(x))

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     return fact
# x = int(input('Enter the no. : '))
# print(f'{i}! = {factorial(x)}')

# def tab(t_no,t_limit):
#     for i in range(1, t_limit+1):
#         print(f"{t_no} x {i} = {t_no*i}")
#     return t_no,t_limit
# t_no = int(input("Enter the table no. : "))
# t_limit = int(input("Enter the table limit: "))
# tab(t_no, t_limit)

# def sum(a, b):
#     result = a + b
#     return result
# no1 = int(input("Enter the value of number 1: "))
# no2 = int(input("Enter the value of number 2: "))
# print(f'The sum of {no1} and {no2} is {sum(no1, no2)}')

# def modify(x):
#     x = x + 1
#     print("Inside",x)
# a = 10
# modify(a)
# print("Outside",a)

# def modify_list(lst):
#     lst.append(42)
#     print("Inside the function:", lst)

# # Example usage
# my_list = [1, 2, 3]
# modify_list(my_list)
# print("Outside the function:", my_list)

# l = [6, 7, 6 , 'Ned', True, (2,4), [4,'nabeed']]
# l.append('Filza')
# l.insert(0,'Sualiha')
# l.pop()
# l.remove('Ned')
# l.reverse()
# print(l.count(6))
# l.clear()
# print(l)

# for i in range(10):
#     for j in range(1,i+1,1):
#         print('*',end=' ')
#     print()
# for i in range(10):
#     for j in range(11,i+1,-1):
#         print('*',end=' ')
#     print()

# for i in range(10):
#     for j in range(1,i+1,1):
#         if i<=8:
#             print(i,end=' ')
#         else:
#             print(j,end=' ')
#     print()
# for i in range(10):
#     for j in range(11,i+1,-1):
#         print('*',end=' ')
#     print()

# for i in range(20):
#     if i <= 10:
#         print(i*'*')
#     else:
#         print((20-i)*'*')

# for i in range(6):
#     for j in range(1,i+1,1):
#         if i == 1 and j == 3:
#             print('*',end=' ')
#     print()
# for i in range(20):
#     if i <= 10:
#         print(i*'*',end=' ')
#     else:
#         print((20-i)*'*',end=' ')
#     print()
# lst = [50,12,4,90,41,22,3,34,56,331,454,32,45]
# n = len(lst)
# for i in range(0,n-1):
#     for j in range(0,n-1-i):
#         if lst[j] > lst[j+1]:
#             temp = lst[j]
#             lst[j] = lst[j+1]
#             lst[j+1] = temp
# print(lst)

# def greed(name):
#     name = f'Hello {name}'
#     print(name)
# greed('Nabeed')
# lst.sort(reverse=True)
# print(lst)
# m = [23,45,65,3]
# x = lst + m
# print(x)
# def fabonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fabonacci(n-2) + fabonacci(n-1)
# for i in range(13):
#     print(fabonacci(i),end=' ')
# for i in range(10):
#     for j in range(1,i+1,1):
#         if i<=3:
#             print(i,end=' ')
#         elif i<=8:
#             if j == 1 or i == j:
#                 print(i,end=' ')
#             else:
#                 print(3,end=' ')
#         else:
#             print(j,end=' ')
#     print()

# def cities():
#     names = []
#     city = input("Enter the name of a city: ")
#     while city != '':
#         names.append(city)
#         city = input("Enter the name of a city: ")
#     print(names)
# cities()

# def acro(p):
#     result = ' '
#     for i in p.split():
#         result = result + i[0].upper()
#     return result
# s = input("Enter the string: ")
# print(acro(s))

# marks = []
# for j in range(3):
#     print(f"Data for {j} rows!!")
#     for i in range(3):
#         m = int(input(f"Enter the marks of {i+1} student: "))
#         marks.append(m)
# print(marks)



# def bubble_sort(lst):
#     n = len(lst)
#     for i in range(0,n-1):
#         for j in range(0,n-1-i):
#             if lst[j] > lst[j+1]:
#                 temp = lst[j]
#                 lst[j] = lst[j+1]
#                 lst[j+1] = temp
#     return lst
# l = []
# for i in range(5):
#     data = int(input(f"Enter the number {i+1}: "))
#     l.append(data)
# print(bubble_sort(l))

# x = (1, 2, 3, 'apple', True)
# y = list(x)
# print(type(y))
# y.pop()
# y.append(False)
# z = tuple(y)
# print(type(z))
# print(z)

# dic = {'name':['Nabeed',0,5,1],'age':19,'Occupation':'Software Engineer','Office':'NJ SE House'}
# print(dic.get('name'))
# for i in dic.keys():
#     print(i)
# for i in dic.values():
#     print(i)
# for x, y in dic.items():
#     print(f'{x} : {y}')

# dic.pop('age')
# print(dic)
# dic.popitem()
# print(dic)
# del dic['Office']
# print(dic)
# try:
#     f = open('file.txt','r')
#     f.read()
#     print(f)
#     f.close()
# except IOError:
#     print('IOError has been occured!')
# try:
#     s = int(input("Enter the number: "))
#     print(s)
# except Exception as e:
#     print(e)
# finally:
#     print("Thank You!!!")
# for i in dic:
#     print(i,':',dic[i])
# s1 = {1,2}
# s2 = {2,1}
# s = s1 == s2
# print(s) 
# d1 = {'name':'Nabeed','age':18}
# d2 = {'age':18,'name':'Nabeed'}
# d = d1 == d2
# print(d)
# l1 = [1,2]
# print(l1[0])
# print(dic['name'][1])
# dic.update({'age':20})
# # print(dic)
# l = ['Nabeed','Ashan','Ayan']
# for i, j in enumerate(l,start=1):
#     print(f'{i}. {j}')
# import math
# # print(dir(math))
# print(type(math.pi))
# try:
#     import nabeed
# except:
#     print("Indentation error occuer")

# family = {'Father':'Jamshed','Mother':'Huma','Sister1':'Sualiha','Sister2':'Filza'}
# g_family = {'Maternal':'Ilyas','Grandma':'Zaitoon',
#             'Paternal':'Chote','Grandma':'Akhtari'}
# family.update(g_family)
# print(family)

# purchased = set()
# price = set()
# my_product = {'Biryani','Lassi','Pizza','Jam','Burger'}
# x = int(input("How many items you want to purchased? "))
# for i in range(x):
#     a = input("Enter the items: ")
#     if a in my_product:
#         my_product.remove(a)
#         purchased.add(a)
#         b = int(input("Enter the price: "))
#         price.add(b)
#     else:
#         print("Sorry your item is out of stock!")
# for j in enumerate(purchased,start=1):
#     print("Your items is: ",j)
# print("Total Amount is: ",sum(price))
# print("The max price is: ",max(price))
# print("The min price is: ",min(price))

# items = {'Biryani','Lassi','Pizza','Jam','Burger'}
# d = {}
# x = []
# for i in range(len(items)):
#     a = items.pop()
#     price = int(input(f"Enter the price of {a}: "))
#     x.append(price)
#     d[a] = price
#     print(price)
# print(d)
# for j in d:
#     print(j,'\t\t\t',d[j])
# print("The Total amount is",sum(x))
# from tkinter import *
# m = Tk()
# f = Frame(m, bg='black', width=300)
# f.pack(fill=Y,side=LEFT)
# m.mainloop()

# with open('file.txt','r') as f:
#     data = f.read()
#     print(data)

# for i in range(1, 10):
#     print((10-i)*' '+i*' *')
# for i in range(1, 10):
#     print(i*' '+(10-i)*' *')

# rows=int(input("Enter number of rows:"))
# column=int(input("Enter number of columns:"))
# m1=[]
# m2=[]

# print("Data for 1st matrix")
# for i in range(rows):
#     row=[]
#     for j in range(column):
#         element=int(input(f"Enter element for {i+1} row {j+1} column:"))
#         row.append(element)
#     m1.append(row)
# print("Data for 2nd matrix")
# for i in range(rows):
#     row = []
#     for j in range(column):
#         element = int(input(f"Enter element for {i + 1} row {j + 1} column:"))
#         row.append(element)
#     m2.append(row)

# result=[]

# if len(m1)==len(m2) and len(m1)!=0:
#     for i in range(len(m1)):
#         rower=[]
#         for j in range(len(m1)):
#             x=m1[i][j]+m2[i][j]
#             rower.append(x)
#         result.append(rower)
# else:
#     print("Addition in not possible because no of rows is not equal to no of column")
# print(result)

# m_result=[[0 for _  in range(column)] for _ in range(rows)]
# for i in range(rows):
#     for j in range(column):
#         for k in range(column):
#             m_result[i][j]=m_result[i][j]+m1[i][k]*m2[k][j]
# print(m_result)

# matrices = []
# matrix_sum = []

# print("Enter data for matrices: ")
# r = int(input("Number of rows: "))
# c = int(input("Number of columns: "))

# for i in range(2):
#     matrix = []
#     for j in range(r):
#         row = []
#         for k in range(c):
#             print(f"Enter data for matrix {i+1}'s {j+1}x{k+1} position",end=' ')
#             row.append(int(input()))
#         matrix.append(row)
#     matrices.append(matrix)
#     print(f"Matrix {i+1} is {matrices[i]}")
# matrix_1, matrix_2 = matrices

# for j in range(len(matrix_1)):
#     sum_row = []
#     for k in range(len(matrix_1[j])):
#         sum_row.append(matrix_1[j][k]+matrix_2[j][k])
#     matrix_sum.append(sum_row)

# print("The sum of the two matrices is: ")
# print(matrix_sum)

# from tkinter import *
# import math as mt
# m =Tk()
# m.title("Calculator")
# m.geometry("700x600")

# def sum():
#     x = float(e1.get())
#     y = float(e2.get())
#     z = x + y
#     label4.config(text=z)
# def sub():
#     x = float(e1.get())
#     y = float(e2.get())
#     z = x - y
#     label4.config(text=z)
# def mult():
#     x = float(e1.get())
#     y = float(e2.get())
#     z = x * y
#     label4.config(text=z)
# def div():
#     x = float(e1.get())
#     y = float(e2.get())
#     z = x / y
#     label4.config(text=z)
# def sqr():
#     x = float(e1.get())
#     z = mt.sqrt(x)
#     label4.config(text=z)
# def factorial():
#     x = int(e1.get())
#     fact = 1
#     if x == 0 or x == 1:
#         fact = fact + 0
#     else:
#         for i in range(1,x+1):
#             fact = fact * i
    
#     label4.config(text=fact)
# def power():
#     x = float(e1.get())
#     z = x**2
#     label4.config(text=z)
# def Table():
#     table_no = int(e1.get())
#     table_range = int(e2.get())
#     for i in range(1, table_range):
#         z = f'{table_no} x {i} = {table_no*i}'
#         Label(m,text=z,bg='black', fg='white',width=15,font=('Time New Roman', 12)).grid(row=i, column=9,padx=10,pady=10)

# label1 = Label(m,text='Enter no 1',bg='black',fg='white',font=(15),width=15,height=2)
# label1.grid(row=2,column=5,padx=20,pady=20)
# label2 = Label(m,text='Enter no 2',bg='black',fg='white',font=(15),width=15,height=2)
# label2.grid(row=3,column=5,padx=20,pady=20)
# label3 = Label(m,text='Result',bg='black',fg='white',font=(15),width=15,height=2)
# label3.grid(row=4,column=5,padx=20,pady=20)
# label4 = Label(m,bg='black',fg='white',font=(15),width=15,height=2)
# label4.grid(row=4,column=7,padx=20,pady=20)

# e1 = Entry(m, bg='grey',fg='black',font=(15),width=15)
# e1.grid(row=2,column=7,pady=10,padx=0)
# e2 = Entry(m, bg='grey',fg='black',font=(15),width=15)
# e2.grid(row=3,column=7,pady=10,padx=0)

# b1 = Button(m,text='Add',bg='black',fg='white',font=(15),width=15,height=2,command=sum)
# b1.grid(row=5,column=5,padx=20,pady=20)
# b2 = Button(m,text='Subtract',bg='black',fg='white',font=(15),width=15,height=2,command=sub)
# b2.grid(row=6,column=5,padx=20,pady=20)
# b3 = Button(m,text='Multiply',bg='black',fg='white',font=(15),width=15,height=2,command=mult)
# b3.grid(row=5,column=7,padx=20,pady=20)
# b4 = Button(m,text='Divide',bg='black',fg='white',font=(15),width=15,height=2,command=div)
# b4.grid(row=6,column=7,padx=20,pady=20)
# b5 = Button(m,text='Factorial',bg='black',fg='white',font=(15),width=15,height=2,command=factorial)
# b5.grid(row=7,column=5,padx=20,pady=20)
# b6 = Button(m,text='Sq_root',bg='black',fg='white',font=(15),width=15,height=2,command=sqr)
# b6.grid(row=7,column=7,padx=20,pady=20)
# b7 = Button(m,text='Square',bg='black',fg='white',font=(15),width=15,height=2,command=power)
# b7.grid(row=8,column=5,padx=20,pady=20)
# b8 = Button(m, text='Table Generator', bg='black', fg='white',font=('Time New Roman',15),width=15,command=Table).grid(row=7,column=7,padx=20,pady=20)

# m.mainloop()

# for i in range(0, 5):
#     k = 1
#     for j in range(0, 6):
#         if j <= i:
#             print(k, end="")
#             k += 1
#         else:
#             print(" ", end="")
#     print()

# for i in range(0, 5):
#     k = 1
#     for j in range(0, 6):
#         if j > i:
#             print(k, end="")
#             k += 1
#         else:
#             print(" ", end="")
#         print()
# import random as rd
# ran_num = rd.randrange(1,10,1)
# rows = 4
# for i in range(10,0,-1):
#     print(i*" *"+" "*(10-i))
# for i in range(0, 6):
#     print(' ' * (5 - i) + '* ' * (i+2))
# for i in range(4,0,-1):
#     print(' '*(4-i) + (i+2)*' *')

# for i in range(1,10):
#     for j in range(1,i+1,1):
#         print('*',end=' ')
#     print()
# for i in range(1, 10):
#     for j in range(10,i+1,-1):
#         print('*',end=' ')
#     print()
# for i in range(20):
#     if i<=10:
#         print(i*'*')
#     else:
#         print((20-i)*'*')
# for i in range(10,0,-1):
#     print(' '*(10-i)+i*'*')
# for i in range(10):
#     print(' '*(10-i)+i*' *')
# for j in range(10):
#     print(' '*j+(10-j)*' *')    

# for j in range(10):
#     print(' '*i+(10-j)*' *')    

# n = int(input("Enter the number: "))
# fact = 1
# if n == 0:
#     print('The factorial of 0! is 0')
# elif n<0:
#     print("factorial should be greater than 1")
# else:
#     for i in range(1, n+1):
#         fact = fact * i
#         print(f"The factorial of {i}! is {fact}")
# sample = [(2,3), (4,7), (8,11), (3,6)]
# x = []
# y = []
# for i in sample:
#     x.append(max(i))
#     y.append(min(i))
# for j in range(len(x)):
#     print(f"Tuple {j+1}")
#     print('Maximum',x[j])
#     print("Minimum",y[j])
# print("Best 5 Students!!")
# s = set()
# for i in range(5):
#     std_names = input(f"Enter the name {i+1} of a students: ")
#     s.add(std_names)
# print("The set of best 5 students is",s)
# def personal_dict():
#     phone_dir = {}
#     for i in range(12):
#         name = input("Enter the name of member"+str(i+1)+':' )
#         phone_no = input("Enter the phone number"+str(i+1)+':')
#         phone_dir[name] = phone_no
#     return phone_dir
# def delete(phone_dir):
#     name = input("Enter the name you want to delete: ")
#     if name in phone_dir:
#         del phone_dir[name]
#     else:
#         print("Element is not in phone directory!")
# def total(phone_dir):
#     total_no = len(phone_dir)
#     print('The total members is',str(total_no))

# phone_dir = personal_dict()
# delete(phone_dir)
# total(phone_dir)
# def hexACI():
#     for char in range(ord('a'), ord('z')+1):
#         acii_value = ord(chr(char))
#         hex_values = format(acii_value, 'x')
#         print(chr(char),':',hex_values)
# hexACI()

# parent_list = ['Nabeed','Ashan', 'Ayan', 'KAmi','Abyaz','Awwab']
# my_list = ['Nabeed','Ashan','Karim','Salman','Hamza','Usman']
# final_list = []
# for i in my_list:
#     if i in parent_list:
#         final_list.append(i)

# print("Number of students in parent list: ",len(parent_list))
# print("Number of students in your list: ",len(my_list))
# print("Number of comman guest: ",len(final_list))
# a =len(parent_list) + len(my_list) - len(final_list)
# print("Total number of guest: ",a)

# i = 0
# while i<=5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print(0)  



class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = x[::-1]
        if x == y:
            print("true")
        else:
            print("false")

x = int(input())
sol = Solution()
y = sol.isPalindrome(x)
   