# s = input().split()
# ns = str(s)
# for i in ns:
#     if i == 5:
#         new = ns.replace(i,'k')
#         print(i,end='')
#     els
        
#         print(i,end='')
# i.replace(i[5],'k')'
# print(''.join(i))
# for i in s:
#     k = i[5]
# print(s.replace(k, 'k'))
# s = input().split()
# for i in s:
#     new = i.replace(i[5],'k')
#     print(new)
# s = input()
# for i in s:
#     if i == i.upper():
#         print(i.lower(),end='')
#     else:
#         print(i.upper(),end='')

# print(s.isupper())
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# result = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
# coordiantes = [cor for cor in result if sum(cor) != n]
# # print(coordiantes)

# string = input()
# sub_string = input()
# count = 0
# for i in range(len(string)-len(sub_string)+1):
#     for j in range(len(sub_string)):
#         if sub_string[j] != string[i+j]:
#             break
#     else:
#         count += 1
# print(count)

# string = input()
# width = int(input())
# for i in range(width):
#     for j in string:
#         if string[i] == width:
#             print(j,'\n')
#         else:
#             break

# string = input()
# for i in range(len(string)-3):
#     for j in string[i:3:3]:
#         if (len(string)-6) == 3:
#             print(string[len(j):i:3],end='')
    
# string = input()
# width = int(input())
# # for i in range(len(s)):
# #     if i == 3:
# #         for j in s[3]:
# #             print(j[i:3:1],end='')
#             # print(string[0:3])
# for i in range(0,len(string),width):
#     print(string[i:i+width])
# string = input()
# max_width = int(input())
# for i in range(0,len(string),max_width):
#     print(string[i:i+max_width])

# n = int(input())
# for i in range(n):
#     a, b = input().split()
#     try:
#         result = int(a) // int(b)
#         print(result)
#     except ZeroDivisionError as e:
#         print("Error Code: ",e)
#     except ValueError as e:
#         print("Error Code: ",e)
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Step 1: Read input for set a
# n1 = int(input())
# a = set()
# s1 = input().split()
# for i in s1:
#     a.add(int(i))

# n2 = int(input())
# b = set()
# s2 = input().split()
# for j in s2:
#     b.add(int(j))
# difference = sorted(a.symmetric_difference(b))
# for i in difference:
#     print(i)

# import math as mt
# a = int(input())
# b = int(input())
# m = int(input())
# c = mt.pow(a,b)
# x = int(c)
# print(x)

# d = c % m
# y = int(d)
# print(y)
# for i in range(1,int(input())):
#     print(i,i-1)
import cmath
import math
# a = float(input())
# b = float(input())
# cmath.phase(complex(a,b))
# r = (a**2) + (b**2)
# s = math.sqrt(r)
# print(s)
# print(cmath.phase(complex(a,b)))
# a = input().split()
# for i in a:
#     if i[1] == '+':
#         b = int(i[0])
#         c = int(i[2])
#         x = (b**2) + (c**2)
#         r = math.sqrt(x)
#         print(r)
#         print(cmath.phase(complex(b,c)))
#     elif i[1] == '-':
#         b = int(i[0])
#         c = int(i[2])
#         x = (b**2) + (c**2)
#         r = math.sqrt(x)
#         print(r)
#         print(cmath.phase(complex(b,-c)))
#     elif i[0] == '-' and i[2] == '-':
#         b = int(i[1])
#         c = int(i[3])
#         x = (b**2) + (c**2)
#         r = math.sqrt(x)
#         print(r)
#         print(cmath.phase(complex(-b,-c)))
#     elif i[0] == '-':
#         b = int(i[1:3])
#         c = int(i[4:6])
#         x = (b**2) + (c**2)
#         r = math.sqrt(x)
#         print(r)
#         print(cmath.phase(complex(-b,c)))

# def bubble_sort(lst,n):
#     for i in range(1, n):
#         for j in range(n-i):
#             if lst[j] > lst[j+1]:
#                 temp = lst[j]
#                 lst[j] = lst[j+1]
#                 lst[j+1] = temp
#     return lst
# l = []
# n = int(input("Enter the number of elements : "))
# for i in range(n):
#     n1 = int(input("Enter the number: "))
#     l.append(n1)    
# print(bubble_sort(l,n))

# l = []
# n = int(input("Enter the number of element: "))
# for i in range(n):
#     n1 = int(input("Enter the no.: "))
#     l.append(n1)
# print("The reverse list is: ",l[::-1])
