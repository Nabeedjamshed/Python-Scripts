# n = int(input())
# l = []
# n1 = input().split()
# for i in n1:
#     n2 = i
#     n3 = int(n2)
#     l.append(n3)
# print(sum(l))

# n = int(input())
# l = []
# n1 = input().split()
# for i in n1:
#     n2 = i
#     n3 = int(n2)
#     l.append(n2)

# positive = []
# negative = []
# zero = []
# leng = len(l)
# for j in l:
#     if j>0:
#         positive.append(j)
#     elif j<0:
#         negative.append(j)
#     else:
#         zero.append(j)

# p = len(positive) / leng
# n = len(negative) / leng
# z = len(zero) / leng
# print('%.6f'%p)
# print('%.6f'%n)
# print('%.6f'%z)

# m = input()
# m = input()
# m = input()
# # m =[11,2,4,
# #     4,5,6,
# #     10,8,-12]
# m1 = m[0] + m[4] + m[8]
# m2 = m[2] + m[4] + m[6]

# m3 = abs(m1 - m2)
# print(m3)

# n = int(input())
# l = []
# n1 = input().split()
# for i in n1:
#     n2 = i
#     n3 = int(n2)
#     l.append(n3)
# c = max(l)
# print(l.count(c))


# l1 = []
# l2 = []
# x = input().split()
# y = input().split()
# Alice = 0
# Bob = 0
# Equal = 0
# for i in x:
#     n2 = i
#     n3 = int(n2)
#     l1.append(n3)
# for j in y:
#     n2 = j
#     n3 = int(n2)
#     l2.append(n3)

# for i in range(len(l1)):
#     if l1[i] > l2[i]:
#         Alice += 1
#     elif l1[i] < l2[i]:
#         Bob += 1
#     else:
#         Equal += 0
# print(Alice,end=' ')
# print(Bob,end=' ')

# l = []
# new = []
# n1 = input().split()
# for i in n1:
#     n2 = i
#     n3 = int(n2)
#     l.append(n3)
# new.append(sum(l)-l[0])
# new.append(sum(l)-l[1])
# new.append(sum(l)-l[2])
# new.append(sum(l)-l[3])
# new.append(sum(l)-l[4])
# print(min(new),end=' ')
# print(max(new),end=' ')

# n = int(input())
# for i in range(n):
#     n1 = int(input())
#     if (n1 > 40) and (n1 % 5 != 0):
#         n1 = round(n1)
#         print(n1)

# n = int(input())
# l = []
# n1 = input().split()
# for k in n1:
#     n2 = k
#     n3 = int(n2)
#     l.append(n3)

# maximum = 0
# minimum = 0
# i = 0
# j = 1
# while j < len(l):
#     if l[i] < l[j]:
#         maximum += 1
#     elif l[i] > l[j]:
#         minimum += 1
#     i += 1
#     j += 1  
# print(maximum,end=' ')
# print(minimum,end=' ')

# import random as r
# n = int(input())
# l = []
# k = int(input())
# n1 = input().split()
# counter = 0
# for i in n1:
#     n2 = i
#     n3 = int(n2)
#     l.append(n3)
# a = l.index()
# b = l.index()
# while b < len(l):
#     if r.choice(l[a]) + r.choice(l[b]) % k == 0:
#         counter += 1
#     else:
#         counter = 0
#     a += 1
#     b += 1
# print(counter)


# n = input().split()
# for i in n:
#     spl_str = i
#     new = int(spl_str)
# l_range = n[0]
# donot_eat = int(n[1])

# l = []
# n1 = input().split()
# for i in n1:
#     n2 = i
#     n3 = int(n2)
#     l.append(n3)
# charged = int(input())
# eat = sum(l) - l[donot_eat]
# mid = eat / 2
# final = charged - mid
# integer = int(final)
# if integer == 0:
#     print("Bon Appetit")
# else:
#     print(int(final))


# n = input().split()
# for i in n:
#     spl_str = i
#     new = int(spl_str)
# no_of_hurdles = int(n[0])
# max_height = int(n[1])

# l = []
# n1 = input().split()
# for i in n1:
#     n2 = i
#     n3 = int(n2)
#     l.append(n3)
# max_list = max(l)
# if max_list > max_height:
#     final = max_list - max_height
#     print(final)
# else:
#     print(0)


# n = input().split()
# for i in n:
#     spl_str = i
#     new = int(spl_str)
# arr_size = int(n[0])
# pairs = int(n[1])

# width = []
# cases = []
# new = []
# n1 = input().split()
# for j in n1:
#     n2 = j
#     n3 = int(n2)
#     width.append(n3)

# for k in range(pairs):
#     n = input().split()
#     for k in n:
#         spl_st = k
#         interger = int(spl_st)
#         cases.append(interger)
# length = len(cases)
# for i in range(0,length,2):
#     if i < length:
#         new.append([cases[i],cases[i+1]])       

# for i in new:
#     for j in i:
#         first = i[0]
#         second = i [1]

#     x = width[first:second+1:1]
#     print(min(x))


# n = input().split()
# for i in n:
#     spl_str = i
#     new = int(spl_str)
# arr_size = int(n[0])
# k = int(n[1])

# l = []
# n1 = input().split()
# for j in n1:
#     n2 = j
#     n3 = int(n2)
#     l.append(n3)
# count = 0
# for i in range(len(l)):
#     for j in i:
#         if (i) + (i+1) % k == 0:
#             count += 1
# print(count)

# keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# values = []
# n1 = input().split()
# for i in n1:
#     n2 = i
#     n3 = int(n2)
#     values.append(n3)
# my_dict = {k: v for k, v in zip(keys, values)}
# string = input()
# length = len(string)

# l = []
# for i in string:
#     if i in my_dict:
#         a = my_dict[i]
#         l.append(a)
# maximum = max(l)
# final = length * maximum
# print(final)

from itertools import*
# lst1 = []
# lst2 = []
# n1 = input().split()
# for i in n1:
#     n2 = i
#     n3 = int(n2)
#     lst1.append(n3)
# n5 = input().split()
# for i in n5:
#     n6 = i
#     n7 = int(n6)
#     lst2.append(n7)
# print(lst1)
# print(lst2)
# cartesian_product = list(product(lst1, lst2))
# for i in cartesian_product:
#     print(i,end=' ')

# s = input().split()
# string = sorted(s[0])
# integer = int(s[1])
# A = list(combinations(string,integer))
# count = 1
# for i in A:
#     if count > integer:
#         print(''.join(i))
#         count += 1
#     else:
#         break


# from collections import Counter
# number_of_shoes = int(input())
# l = []
# n1 = input().split()
# for i in n1:
#     n2 = i
#     n3 = int(n2)
#     l.append(n3)
# number_of_customers = int(input())
# new = []
# for i in range(number_of_customers):
#     values_of_the_shoe_size_and_price = input().split()
#     size = values_of_the_shoe_size_and_price[0]
#     price = values_of_the_shoe_size_and_price[1]
#     new.append(price)
# lst = []
# for j in new:
#     integer = int(j)
#     lst.append(integer)
# print(lst)
# print(sum(lst))
# keys = Counter(l).keys()
# values = Counter(l).values()
# print(keys)
# print(values)



# n = int(input())
# l = set()
# n1 = input().split()
# for i in n1:
#     n2 = i
#     n3 = int(n2)
#     l.add(n3)
# result = (sum(l) / len(l))
# print(result)

# def average(array):
#     s = set()
#     for i in array:
#         s.add(i)
#         r = (sum(s)/len(s))
#     return r
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)

# n1 = int(input())
# s1 = set(map(int, input().split()))
# n2 = int(input())
# s2 = set(map(int, input().split()))
# s3 = s1.union(s2)
# print(len(s3))

# n = int(input())
# for i in range(n):
#     test1 = int(input())
#     l = set()
#     n1 = input().split()
#     for i in n1:
#         l.add(i)
#     test2 = int(input())
#     l1 = set()
#     n2 = input().split()
#     for j in n2:
#         l1.add(j)
#     if l in l1:
#         print("True")
#     else:
#         print("False")


# n = int(input())
# s = set()
# n1 = input().split()
# for i in n1:
#     n2 = i
#     n3 = int(n2)
#     s.add(n3)
# runner = sorted(s,reverse=True)
# print(runner[1])


# n = int(input())
# name = []
# grade = []
# for j in range(n):
#     na = input()
#     n1 = float(input())
#     name.append(na)
#     grade.append(n1)

# my_dict = {k: v for k, v in zip(name, grade)}
# first = sorted(grade)
# first1 = first[1]
# second1 = first[2]
# new = []
# new2 = []
# new3 = []
# for i,j in my_dict.items():
#     if first1 == second1:
        
#         if j == first1 or j == second1:
#             new.append(i)
#         new1 = sorted(new)
        
    
#     elif j == first1:
#         new2.append(i)
#         new3 = sorted(new2)
#         for i in new3:
#             print(i)
# if first1 == second1:       
#     for k in new1:
#         print(k)
# else:
#     pass


# if __name__ == '__main__':
#     students = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])
#     print(students)

#     # Sort the students based on their grades
#     students.sort(key=lambda x: (x[1], x[0]))

#     # Find the second lowest grade
#     second_lowest_grade = None
#     for i in range(1, len(students)):
#         if students[i][1] > students[0][1]:
#             second_lowest_grade = students[i][1]
#             break

#     # Print names with the second lowest grade
#     for student in students:
#         if student[1] == second_lowest_grade:
#             print(student[0])


# n = int(input())
# l = []
# for i in range(n):
#     n1 = input().split()
#     if n1[0] == 'insert':
#         l.insert(int(n1[1]),int(n1[2]))
#     elif n1[0] == 'print':
#         print(l)
#     elif n1[0] == 'remove':
#         l.remove(int(n1[1]))
#     elif n1[0] == 'append':
#         l.append(int(n1[1]))
#     elif n1[0] == 'sort':
#         l.sort()
#     elif n1[0] == 'pop':
#         l.pop()
#     elif n1[0] == 'reverse':
#         l.reverse()

# s = input()
# small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# numbers = [0,1,2,3,4,5,6,7,8,9]
# for i in s:
#     if i in small:
#         s1 = s.isalnum()
#         print(s1)
#     elif i in small or capital:
#         s2 = s.isalpha()
#         print(s2)
#     elif i in numbers:
#         s3 = s.isdigit()
#         print(s3)
#     elif i in small:
#         s4 = s.islower()
#         print(s4)
#     elif i in capital:
#         s5 = s.isupper()
#         print(s5)

# from collections import deque
# d = deque()
# n = int(input())
# for i in range(n):
#     s = input().split()
#     if s[0] == 'append':
#         d.append(s[1])
#     elif s[0] == 'appendleft':
#         d.appendleft(s[1])
#     elif s[0] == 'pop':
#         d.pop()
#     elif s[0] == 'popleft':
#         d.popleft()
# for i in d:
#     print(i,end=' ')

# n = int(input())
# l = []
# same = []
# notsame = []
# distinct = []
# for i in range(n):
#     s = input()
#     l.append(s)

# for i in l:
#     count = l.count(i)
#     if count > 1 and i not in same:
#         same.extend([i]*count)

# for i in l:
#     for j in same:
#         if i != j and i not in notsame:
#             notsame.append(i) 
# for k in l:
#     if k not in distinct:
#         distinct.append(k)
# print(len(distinct))
# print(len(same),end=' ')
# for i in notsame:
#     print(notsame.count(i),end=' ')


# countries = ['spain', 'france', 'germany', 'norway']
# capitals = ['madrid', 'paris', 'berlin', 'oslo']

# # Get index of 'germany': ind_ger

# ind_ger = countries.index("germany")
# new = capitals[ind_ger]
# print(new)
# print(ind_ger)

# europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# # Print out the keys in europe
# for i in europe.keys():
#     print(i)
# print(europe['norway'])

# Definition of dictionary
# europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# # Add italy to europe
# europe["italy"] = 'rome'

# # Print out italy in europe
# print('italy' in europe) # it return True

# # Add poland to europe
# europe['poland'] = 'warsaw'

# # Print europe
# print(europe)

# Dictionary of dictionaries
# europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
#            'france': { 'capital':'paris', 'population':66.03 },
#            'germany': { 'capital':'berlin', 'population':80.62 },
#            'norway': { 'capital':'oslo', 'population':5.084 } }


# # Print out the capital of France
# print(europe['france']['capital'])

# # Create sub-dictionary data

# data = {'capital' : 'rome', 'population' : 59.83}

# # Add data to europe under key 'italy'
# europe['italy'] = data

# # Print europe
# print(europe)


# import pandas as pd

# # Build cars DataFrame
# names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
# dr =  [True, False, False, False, True, True, True]
# cpc = [809, 731, 588, 18, 200, 70, 45]
# cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
# cars = pd.DataFrame(cars_dict)
# print(cars)

# # Definition of row_labels
# row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# # Specify row labels of cars
# cars.index = row_labels

# # Print cars again
# print(cars)

# CSV to DataFrame (2)
# Your read_csv() call to import the CSV data didn't generate an error, but the output is not entirely what we wanted. The row labels were imported as another column without a name.

# Remember index_col, an argument of read_csv(), that you can use to specify which column in the CSV file should be used as a row label? Well, that's exactly what you need here!

# Python code that solves the previous exercise is already included; can you make the appropriate changes to fix the data import?

# Instructions
# 100 XP
# Run the code with Run Code and assert that the first column should actually be used as row labels.
# Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
# Has the printout of cars improved now?


# Import pandas as pd
# import pandas as pd

# # Fix import by including index_col
# cars = pd.read_csv('cars.csv',index_col=0)

# # Print out cars
# # print(cars)

# import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# # Extract drives_right column as Series: dr
# dr = cars['drives_right']


# # Use dr to subset cars: sel
# sel = cars[dr]

# # Print sel
# print(sel)

# # Import cars data
# import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)
# # Create car_maniac: observations that have a cars_per_cap over 500
# cpc = cars['cars_per_cap']
# many_cars = cpc>500
# car_maniac = cars[many_cars]
# print(car_maniac)

# import numpy as np
# heigth = np.array([1.2,4.5,3.2,4.7])
# weight = np.array([5.8,9.8,7.2,3.6])
# result = np.array([heigth,weight])
# # for i in np.nditer(result): ye just like nested loop ka kaam kedega. nditer is a function. dictionary require a method numpy array use a function
# for i in result:
#     for j in i:
#         print(j)


# 


#!/bin/python3


# n = int(input())
# new = []
# for i in range(n):
#     n1 = list(map(int, input().split()))
#     new.append(n1)
# k = 0
# diagnol1 = []
# for i in new:
#     d = i[k]
#     k += 1
#     diagnol1.append(d)

# k = -1
# diagnol2 = []
# for i in new:
#     d = i[k]
#     k -= 1
#     diagnol2.append(d)

# sum1 = sum(diagnol1)
# sum2 = sum(diagnol2)
# difference = sum1 - sum2
# result = abs(difference)
# print(result)



# s = input()
# s1 = list(s)
# if s1[-2] == 'P':
#     print(s)
# elif s1[0] == '1' and s[1] == '2':
#     pass
# else:
#     for i in s:
#         if i[1] != 2:
#             integer1,integer2 = int(i[0]),int(i[1])
#     r = s[0] * 12
#     print(r)


# n = int(input())
# n1 = input().split()
# maximum = []
# minimum = []
# max_count = 0
# min_count = 0
# for i in n1:
#     n2 = i
#     n3 = int(n2)
#     maximum.append(n3)
#     minimum.append(n3)

# for i in maximum:
#     pass
# for j in minimum:
#     # pass

#     if maximum[i] > minimum[j]:
#         max_count += 1
#         i += 1
#         # j += 1
#     elif maximum[i] == minimum[j]:
#         max_count = 0
#         min_count = 0
#         i += 1
#         if i not in maximum:
#             break
#         # j += 1
#     else:
#         min_count += 1
#         # i += 1
#         j += 1


# q = int(input()) 

# inputs = [] 

# for _ in range(q):
#     xyz = input().split()
#     inputs.append((int(xyz[0]), int(xyz[1]), int(xyz[2])))

# for x, y, z in inputs:
#     if abs(x - z) < abs(y - z):
#         print("Cat A")
#     elif abs(y - z) < abs(x - z):
#         print("Cat B")
#     else:
#         print('Mouse C')


# l1 = []

# n1 = list(map(int, input().split()))           
# n2 = list(map(int, input().split())) 

# l1.append(n1)
# l1.append(n2)
# l = l1[0]+l1[1]
# print(sorted(l))

# class Solution:
#     def mergeTwoLists(self, list1, list2):
#         self.l = []
#         self.l1 = list1
#         self.l2 = list2
#         self.l.append(n1)
#         self.l.append(n2)
#         self.new_l = self.l[0]+self.l[1]
#         print(sorted(self.new_l))

# n1 = list(map(int, input().split()))           
# n2 = list(map(int, input().split())) 

# n = Solution()
# n.mergeTwoLists(n1,n2)


# def isPalindrome(num):
#     original_num = num
#     reversed_num = 0
#     if num < 0:
#         num = abs(num)
#     while num != 0:
#         digit = num % 10  
#         reversed_num = reversed_num * 10 + digit  
#         num //= 10 
#     if original_num < 0:
#         print('false')
#     else:
#         if original_num == reversed_num:
#             print('true')
#         else:
#             print('false')
       
# num = int(input())
# isPalindrome(num)

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         original_num = x
#         reversed_num = 0
#         if x < 0:
#             x = abs(x)
#         while x != 0:
#             digit = x % 10  
#             reversed_num = reversed_num * 10 + digit  
#             x //= 10 
#         if original_num < 0:
#             return False
#         else:
#             if original_num == reversed_num:
#                 return True
#             else:
#                 return False


# x = int(input())
# s = Solution()
# s.isPalindrome(x)



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# def tribonacci(n: int) -> int:
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

# num = int(input("Enter the number: "))
# print(tribonacci(num))

# def merge(l,r):
#     new = []
#     i,j = 0,0
#     while i<len(l) and j < len(r):
#         if l[i] < r[j]:
#             new.append(l[i])
#             i += 1
#         else:
#             new.append(r[j])
#             j += 1
#     new.extend(l[i:])
#     new.extend(r[j:])
#     return new

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[mid:]
#     right = arr[:mid]
#     l_left = merge_sort(left)
#     r_rigth = merge_sort(right)
#     return merge(l_left,r_rigth)

# l = list(map(int, input().split()))
# print(merge_sort(l))
 


# def bubble_sort(n):
#     size = len(n)
#     for i in range(0,size):
#         for j in range(0, size-i-1):
#             if n[j] > n[j+1]:
#                 temp = n[j]
#                 n[j] = n[j+1]
#                 n[j+1] = temp
#     return n
# l = list(map(int, input().split()))
# print(bubble_sort(l))


# def binary_search(arr,target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if mid == target:
#             return mid
#         elif mid < target:
#             return mid + 1
#         else:
#             return mid - 1
#     return -1

# l = list(map(int, input().split()))
# tar = int(input())
# r = binary_search(l,tar)

# if (r != -1):
#     print(f"Your target number {tar} is found at {r} index")
# else:
#     print(f"Your target number is not found")



# def linear_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# l = list(map(int, input().split()))
# tar = int(input())
# r = linear_search(l,tar)

# if (r != -1):
#     print(f"Your target number {tar} is found at {r} index")
# else:
#     print(f"Your target number is not found")



# class Solution:
#     def romanToInt(self, s: str) -> int:
#         self.dic = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
#         self.total = 0
#         self.keys = []
#         for i in s:
#             if i in self.dic.keys():
#                 self.keys.append(i)
#                 self.total += self.dic[i]
#         for j in range(len(self.keys)-1):
#             if (self.keys[j] == 'I') and ('V' in self.keys[j+1:]):
#                 self.total -= 2
#             if (self.keys[j] == 'I') and ('X' in self.keys[j+1:]):
#                 self.total -= 2
#             if (self.keys[j] == 'X') and ('L' in self.keys[j+1:]):
#                 self.total -= 20
#             if (self.keys[j] == 'X') and ('C' in self.keys[j+1:]):
#                 self.total -= 20
#             if (self.keys[j] == 'C') and ('D' in self.keys[j+1:]):
#                 self.total -= 200
#             if (self.keys[j] == 'C') and ('M' in self.keys[j+1:]):
#                 self.total -= 200
#         return self.total


# class Solution:
#     def romanToInt(self, s: str) -> int:
#         self.dic = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
#         self.total = 0
#         for i in s:
#             if i in self.dic.keys():  
#                 self.total += self.dic[i]
#         return self.total



# class Solution:
#     def reverse(self, x: int) -> int:
#         self.original_num = x
#         self.reversed_num = 0
#         self.x = abs(x)
#         while self.x != 0:
#             self.digit = self.x % 10  
#             self.reversed_num = self.reversed_num * 10 + self.digit  
#             self.x //= 10 
#         if self.original_num > 0:
#             return self.reversed_num
#         else:
#             self.result = int(f'-{self.reversed_num}')
#             return self.result


# def twoSum(nums: list[int], target: int):
    # nums = list(map(int,input().split()))
    # target = int(input())
    
    # i,j = 0,0
    # l = []
    # while i<len(nums):
    #     if (nums[i] == nums[j]) and (nums[i]+nums[j] == target):
    #         l.append(nums[i])
    #         l.append(nums[j])
            

    #     elif (nums[i] + nums[j+1] == target):
    #         l.append(nums[i],nums[j+1])
    #     else:
    #         i += 1
    #         j += 1
    # print(l)
#     mid = len(nums) // 2
#     left = nums[mid:]
#     right = nums[:mid]
#     while i<len(left) and j<len(right):
#         if left[i]+right[j] == target:
#             l.append(left[i])
#             l.append(right[j])
#         elif left[i]+right[j] != target:
#             j += 1
#             if left[i]+right[j] == target:
#                 i += 1
        

#     print(l)
    
# nums = list(map(int,input().split()))
# target = int(input())
# twoSum(nums,target)


# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         self.s1 = s.split()
#         self.l = int(len(self.s1[-1]))
#         return self.l



# l = list(map(str, input().split()))
# for i in range(len(l)-1):
#     if (l[i][0] and l[i][1]) == (l[i+1][0] and l[i+1][1]):
#         print(l[i][0],end='')
#         print(l[i][1])
#         break
#     else:
#         print(str())


# l = list(map(int, input().split()))
# a_string = [str(i) for i in l]
# a_string_join = "".join(a_string)
# a_string_int = int(a_string_join)
# a_string_add = a_string_int + 1
# s = str(a_string_add)
# a = [int(x) for x in s]
# return a

# class Solution:
#     def plusOne(self, digits: list[int]) -> list[int]:
#         self.a_string = [str(self.i) for self.i in self.digits]
#         self.a_string_join = "".join(self.a_string)
#         self.a_string_int = int(self.a_string_join)
#         self.a_string_add = self.a_string_int + 1
#         self.s = str(self.a_string_add)
#         self.a = [int(self.x) for self.x in self.s]
#         return self.a

# import math as m
# def mySqrt(x: int) -> int:
#     sq = m.sqrt(x)
#     c_sq = m.floor(sq)
    # print(c_sq)
# x = int(input())
# mySqrt(x)

# import math as m
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         self.sq = m.sqrt(x)
#         self.c_sq = m.floor(self.sq)
#         return self.c_sq

# max_marks_names = {}
# max_marks = []
# for i in range(3):
#     print("Enter details of student",i+1)
#     roll_number = int(input("Enter the roll number: "))
#     name = input("Enter the name: ")
#     age = int(input("Enter the age: "))
#     marks = int(input("Enter the marks: "))
#     max_marks_names[name] = marks
#     max_marks.append(marks)
#     print()
#     print("Roll Number: ",roll_number)
#     print("Name: ",name)
#     print("Age: ",age)
#     print("Marks: ",marks)
#     print()
# m = max(max_marks)
# for x,y in max_marks_names.items():
#     if y == m:
#         print("The name of a student is ",x,"and maximum marks is ",m)
#         break
#     else:
#         print(None)
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         l3 = []
#         for i in list1:
#             l3.append(i)
#         for j in list2:
#             l3.append(j)
#         l4 = sorted(l3)
#         return l4


# from itertools import permutations
# l = list(map(int, input().split()))
# perm = permutations(l)
# l3 = []
# l2 = set()
# for i in perm:
#     l2.add(i)
# for j in l2:
#     l3.append(list(j))
# print(l3)


# from itertools import permutations
# class Solution:
#     def permute(self, nums: list[int]) -> list[list[int]]:
#         self.perm = permutations(nums)
#         self.l2 = []
#         for i in self.perm:
#             self.l2.append(list(i))
#         return self.l2

# l = []
# nums = list(map(int, input().split()))
# target = int(input())
# nums.append(0)
# print(nums)
# for i in range(len(nums)-1):
    
#     if nums[i]+nums[i+1] == target:
#         l.append(i)
#         l.append(i+1)
# print(l)


# nums = list(map(int, input().split()))
# target = int(input())
# i,j = 0,1
# l = []
# while j<(len(nums)):
#     if nums[j] in l:
#         first = nums[i]
#         second = nums[j]
#         if first+second==target:
#             l.append(i)
#             l.append(j)
#     else:
#         j+=1
#         first = nums[i]
#         second = nums[j]
#         if first+second==target:
#             l.append(i)
#             l.append(j)
# print(l)
# import math as m
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         if divisor < 0 and dividend < 0:
#             self.d = m.ceil(dividend/divisor)
#             if self.d < (2**31-1):
#                 self.d = self.d
#             elif self.d > (2**31):
#                 self.d = self.d-1
#         elif divisor < 0 :
#             self.d = m.ceil(dividend/divisor)
#             if self.d > (2**31-1):
#                 self.d = self.d-1
#             elif self.d < (2**31):
#                 self.d = self.d
#         else:
#             self.d = m.floor(dividend/divisor)
#             if self.d > (2**31-1):
#                 self.d = self.d-1
#             elif self.d < (2**31):
#                 self.d = self.d
#         return self.d
# dividend = int(input())
# divisor = int(input())
# print(divide(dividend,divisor))



# import math as m
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         if divisor < 0 and dividend < 0:
#             self.d = m.ceil(dividend/divisor)
#             if self.d > (2**31-1):
#                 self.d = self.d-1
#             elif self.d < (2**31):
#                 self.d = self.d-1
#         elif divisor < 0 :
#             self.d = m.ceil(dividend/divisor)
#             if self.d > (2**31-1):
#                 self.d = self.d-1
#             elif self.d < (2**31):
#                 self.d = self.d
#         else:
#             self.d = m.floor(dividend/divisor)
#             if self.d > (2**31-1):
#                 self.d = self.d-1
#             elif self.d < (2**31):
#                 self.d = self.d
#         return self.d

# import math as m
# x = float(input())
# n = int(input())
# ans = m.pow(x,n)
# f = round(ans,5)
# print(f)


# import math as m
# l1 = list(map(int, input().split()))
# l2 = list(map(int, input().split()))
# l = l1+l2
# sorted_l = sorted(l)
# if len(sorted_l) % 2 != 0:
#     mid = (m.ceil(float(len(sorted_l) / 2)) - 1)
#     ans = sorted_l[mid]
# else:
#     mid_l = int((len(sorted_l)) / 2)
#     ans1 = sorted_l[mid_l]
#     ans2 = sorted_l[(mid_l)-1]
#     ans = (ans1 + ans2) / 2
# print(ans)

# l = []
# s = input()
# for i in range(len(s)):
#     if s[i] not in l:
#         l.append(s[i])
# if s == " ":
#     l.append(1)
#     length = len(l) 
# elif s == "":
#     l = []
#     length = len(l) 
# else:
#     length = len(l)        
# print(length)

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         self.l = []
#         for i in range(len(s)):
#             if s[i] not in self.l:
#                 self.l.append(s[i])
#         if s == " ":
#             self.l.append(1)
#             self.length = len(self.l) 
#         elif s == "":
#             self.l = []
#             self.length = len(self.l) 
#         else:
#             self.length = len(self.l)        
        
#         return self.length


# nums = list(map(int, input().split()))
# target = int(input())
# for i in nums:
#     if target == i:
#         ans = nums.index(target)
# else:
#     nums.append(target)
#     sorted_l = sorted(nums)
#     for i in sorted_l:
#         if target == i:
#             ans = sorted_l.index(target)
# print(ans)

# l = []
# nums = []
# n = int(input("Enter total numbers in array: "))
# for i in range(n):
#     num = int(input("Enter the value of array: "))
#     nums.append(num)
# for i in nums:
#     if i not in l:
#         l.append(i)
# print(l)

# haystack = input()
# needle = input()
# if needle in haystack:
#     index = haystack.index(needle)
# else:
#     index = -1
# print(index)

# l = []
# nums = list(map(int, input().split()))
# target = int(input())
# for i in nums:
#     if target in nums:
#         l.append(i)
# print(l)

# l = []
# nums = list(map(int, input().split()))
# target = int(input())
# for i in range(len(nums)):
#     if target == nums[i]:
#         l.append(i)
# if len(l) == 1:
#     l.append(0)
# if target not in nums:
#     l.append(-1)
#     l.append(-1)
# print(l)

# l1 = list(map(int, input().split()))
# m = int(input())
# l2 = list(map(int, input().split()))
# n = int(input())
# three_element = l1[0:m:1]
# for i in three_element:
#     l2.append(i)
# ans = sorted(l2)
# print(ans)

# l1 = list(map(int, input().split()))
# m = int(input())
# l2 = list(map(int, input().split()))
# n = int(input())
# l1= l1[0:m:1]
# for i in l2:
#     l1.append(i)
# l1 = sorted(l1)
# print(l1)

# l = []
# l1 = list(map(str, input().split()))
# l2 = list(map(str, input().split()))
# l3 = list(map(str, input().split()))
# l.append(l1)
# l.append(l2)
# l.append(l3)
# word = input()
# for i in word:
#     for j in i:

#         print('true')
#         break
#     if i in l2:
#         print('true')
#         break
#     if i in l3:
#         print('true')
#         break
#     else:
#         print('false')

# from itertools import combinations
# l = []
# k = int(input())
# n = int(input())
# for i in range(1,n+1):
#     l.append(i)
# l1 = []
# ans = list(combinations(l,k))
# # for j in ans:
# #     if sum(j) == n:
# #         l1.append(list(j))
# print(l1)

# l1 = []
# l = list(map(int, input().split()))
# i,j = 0,1
# while i<=len(l):
#     if l[i] != l[j]:
#         # l.remove(l[i])
#         # l.remove(l[j])
#         j += 1
#     l1.append(l[i])
#     i+=1
#     j+=1
# else:
    
#     i += 1
#     j+=1
# print(l)
# # print(l1)

# l = list(map(int, input().split()))
# n = len(l)
# for i in range(n+1):
#     if i not in l:
#         a = i
# print(a)

# import inflect
# start = inflect.engine()

# num = int(input())

# number_to_word = start.number_to_words(num)
# print(number_to_word)

# class Solution:
#     def addDigits(self, num: int) -> int:
#         if num < 10:
#             return num
#         else:
#             self.l = []
#             self.nums = str(num)
#             for i in self.nums:
#                 self.l.append(int(i))
#             self.sum_l = sum(self.l)
#             return self.addDigits(self.sum_l)
        
# import math as m
# n = int(input())
# if n == 1:
#     print('true')
# else:
#     sq = m.sqrt(n)
#     power = (2**sq)
#     print(power)
#     new = m.ceil(power)
#     if new == n:
#         print('true')
#     else:
#         print('false')

# n = int(input())
# sum = 1
# while sum < n:
#     sum = sum * 3
# if sum == n:
#     print('true')
# else:
#     print('false')


# l = list(map(int, input().split()))
# l1 = set()
# for i in l:
#     l1.add(i)
# if len(l) != len(l1):
#     print('true')
# else:
#     print('false')


# s = input().split()
# new = list(s[::-1])
# new_s = " ".join(new)
# print(type(new_s))

# version1 = input()
# version2 = input()
# version3 = float(version1.rstrip(str).rstrip(str))
# version4 = float(version2.rstrip(str).rstrip(str))
# version5 = int(version3)
# version6 = int(version4)

# if version5 < version6:
#     print(-1)
# elif version5 > version6:
#     print(1)
# else:
#     print(0)


# nums = list(map(int, input().split()))
# k = int(input())
# new = nums[-1:(-k-1):-1]
# sorted_new = sorted(new)
# for i in sorted_new:
#     nums.remove(i)
# ans = sorted_new + nums
# print(ans)

# l = []
# s1 = set()
# s2 = set()
# num1 = list(map(int, input().split()))
# num2 = list(map(int, input().split()))
# for i in num1:
#     s1.add(i)
# for j in num2:
#     s2.add(j)
# ans = s1.intersection(s2)
# for k in ans:
#     l.append(k)
# print(l)

# s = set()
# num1 = list(map(int, input().split()))
# num2 = list(map(int, input().split()))
# k = int(input())
# for i in num1:
#     num2.append(i)
# new = sorted(num2,reverse=True)

# for j in new:
#     s.add(j)
# s1 = sorted(s,reverse=True)
# ans = s1[:k:1]
# print(ans)

# l = []
# nums = list(map(int, input().split()))
# for i in nums:
#     if nums.count(i) >= 2:
#         l.append(i)

# for j in l:
#     a = j
# print(a)


    # n = int(input())
    # fact = 1
    # for i in range(1,n+1):
    #     fact = fact*i

    # digits = []
    # new = digits
    # while fact > 0:
    #     digit = fact % 10  
    #     digits.insert(0, digit)  
    #     fact //= 10  

    # print(new)
    # if 0 in digits:
    #     digits.remove(0)
    # print(digits)
    # if len(new) > len(digits):
    #     print(0)


# n = int(input())
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i

# digits = []
# while fact > 0:
#     digit = fact % 10  
#     digits.insert(0, digit)  
#     fact //= 10  
# new = digits.copy()
# while digits[-1] == 0:
#     digits.pop()
# l = []
# for j in range(len(new) - len(digits)):
#     l.append(0)

# print(l.count(0))


# import re
# s = input()
# new_s = re.sub(r"[^\w]", "",s)
# print(new_s)
# new_lower = new_s.lower()
# reverse_new_lower = new_lower[::-1]

# if new_lower == reverse_new_lower:
#     print('true')
# else:
#     print('false')



# def twoSum(numbers: list[int], target: int):
#     l = []
#     for i in range(len(numbers)):
#         for j in range(i+1,len(numbers)):
#             if numbers[i]+numbers[j] == target:
#                 l.append(i)
#                 l.append(j)
#     l1 = []
#     for k in l:   
#         sums = k+1
#         l1.append(sums)
#     return l1
# nums = list(map(int, input().split()))
# tar = int(input())
# a = twoSum(nums,tar)
# print(a)

# l = []
# nums = list(map(int, input().split()))
# for i in nums:
#     a = nums.count(i)
#     if a > (len(nums) / 3) and i not in l:
#         l.append(i)
# print(l)


# l = []
# n = int(input())
# for i in range(n+1):
#     l.append(i)
# digits = []
# for j in l:
#     while j > 9:
#         digit = j % 10  
#         digits.insert(0, digit)  
#         j //= 10  
# print(l)
# print(digits)

# l = []
# s = set()
# nums = list(map(int, input().split()))
# for i in nums:
#     if nums.count(i) > 1:
#         l.append(i)
# for j in l:
#     s.add(j)
# for k in s:
#     a = k
# print(a)

# l = []
# number = int(input())
# binary_number = hex(number)[2:]
# print(binary_number)
# for i in binary_number:
#     if i == '1':
#         l.append('0')
#     else:
#         l.append('1')
# a = "".join(l)
# ans = int(a,2)
# print(ans)

# l = []
# nums = list(map(int, input().split()))
# for i in range(1,len(nums)+1):
#     if i not in nums:
#         l.append(i)
# print(l)

# l = []
# nums = list(map(int, input().split()))
# for i in nums:
#     if nums.count(i) > 1 and i not in l:
#         l.append(i)
# ans = sorted(l)
# print(ans)


# def thirdMax(nums: list[int]):
#     s =set()
#     for i in nums:
#         s.add(i)
#     if len(s) < 3:
#         new = max(s)
#         return new
#     else:
#         l = list(s)
#         ans = sorted(l)
#         new = ans[-3]
#         return new
# nums = list(map(int, input().split()))
# a = thirdMax(nums)
# print(a)

# l = []
# a = int(input())
# b = list(map(int, input().split()))
# for i in b:
#     l.append(str(i))
# c = "".join(l)
# integer_c = int(c)
# new = pow(a,integer_c) % 1337
# print(new)


# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-2)+fib(n-1)


# s = input()
# if s == s.upper():
#     print('true')
# else:
#     print('false')

# l = []
# nums = list(map(int, input().split()))
# for i in nums:
#     if nums.count(i) < 2:
#         l.append(i)
# for j in l:
#     a = j
# print(a)

# l = []
# s = input().split()
# for i in s:
#     l.append(i)
# reversed_string = []
# for j in l:
#     new = j[::-1]
#     reversed_string.append(new)
# ans = " ".join(reversed_string)
# print(ans)

# lower = []
# upper = []
# s = input()
# for i in s:
#     if i == i.lower():
#         lower.append(i)
#     else:
#         a = i.lower()
#         upper.append(a)

# for i in lower:
#     if i != 'c':
#         print(0)
# for j in upper:
#     if j != 'c':
#         print(0)
# else:
#     new_upper = set(upper)
#     c = 0
#     for j in new_upper:
#         if j in lower: 
#             c += 1
# print(c)

# l = []
# s = input()
# for i in s:
#     a = ord(i)
#     l.append(a)
# new = []
# for j in range(len(l)-1):
#     ans = l[j] - l[j+1]
#     answer = abs(ans)
#     new.append(answer)
# x = sum(new)
# print(x)

# s = input()
# s1 = s.lower()
# count = 0
# for i in range(len(s)-1):
#     if s1[i] != s1[i+1]:
#         count += 1
# print(count)


# s = input()
# s1 = s.count(s[0])
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         print(-1)
# else:
#     if s1 == 1:
#         print(0)
#     else:
#         print(s1)

# l = []
# x = int(input())
# string_x = str(x)
# for i in string_x:
#     l.append(int(i))
# divider = sum(l)
# if x % divider == 0:
#     print(divider)
# else:
#     print(-1)


# l = []
# nums = list(map(int, input().split()))
# if len(nums) <= 10000 and len(nums) >= 3:
#     for j in nums:
#         l.append(abs(j))
#     sorted_nums = sorted(l)
#     new_nums = sorted_nums[-3:]
#     mult = 1
#     for i in new_nums:
#         mult = mult * i
# elif len(nums) <= 10000 and len(nums) >= 3:

# l = []
# word1 = input()
# word2 = input()
# if word1 == word2:
#     print(0)
# else:
#     for i in word1:
#         for j in word2:
#             if i == j:
#                 l.append(i)
#     s = set()
#     for i in l:
#         s.add(i)
#     print(len(s))


# nums = list(map(int, input().split()))
# s = set()
# for i in nums:
#     s.add(i)
# l = []
# l1 = []
# for j in s:
#     l.append(j)
#     l1.append(j)
# if len(nums) > len(l):
#     l.append('_')
# print(len(l1))
# print(l)

# from itertools import*
# l = set()
# s = []
# word = input()
# for i in word:
#     s.append(i)
# ans = list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))
# for i in ans:
#     l.add(i)
# l1 = []
# for j in l:
#     l1.append(list(j))
# print(l1)

# nums = list(map(int, input().split()))
# indexDiff = int(input())
# valueDiff = int(input())
# if valueDiff != indexDiff:
#     if abs(valueDiff - indexDiff) <= indexDiff:
#         if abs(nums[valueDiff] - nums[indexDiff]) <= valueDiff:
#             print('true')
#         else:
#             print('false')
#     else:
#         print('false')
# else:
#     print('false')

# answer = []
# n = int(input())
# for i in range(1,n+1):
#     if (i % 3 == 0) and (i % 5 == 0):
#         answer.insert(i,"FizzBuzz")
#     elif (i % 3) == 0:
#         answer.insert(i,"Fizz")
#     elif (i % 5) == 0:
#         answer.insert(i,"Buzz")
#     else:
#         answer.insert(i,str(i))
# print(answer)

# s = set()
# word = input()
# ch = input()
# if ch not in word:
#     print(word)
# else:
#     for i in word:
#         if i == ch:
#             s.add(word.index(i))
#     number = s.pop()
#     new = word[0:(number+1):1]
#     new_word1 = new[::-1]
#     new_word2 = word[(number+1)::1]
#     ans = new_word1+new_word2
#     print(ans)

# s=set()
# num1 = list(map(int, input().split()))
# num2 = list(map(int, input().split()))
# sorted_num1 = sorted(num1)
# sorted_num2 = sorted(num2)
# for i in range(len(num1)):
#     num = sorted_num2[i] - sorted_num1[i]
#     s.add(num)
# s1 = s.pop()
# print(s1)

# arr = []
# num = list(map(int, input().split()))
# if len(num) == 2:
#     ans = sorted(num,reverse=True)
#     print(ans)
# else:
#     new_num = sorted(num)
#     mid = len(new_num) // 2
#     left = new_num[:mid]
#     right = new_num[mid:]
#     sorted_left = sorted(left,reverse=True)
#     sorted_right = sorted(right,reverse=True)
#     ans = sorted_left+sorted_right
#     print(ans)
# print(left)
# print(right)
# for i in range(len(num)//2):
#     l.append(new_num[i])
# for i in range(len(num)//2):

# l = []
# s = input().split()
# k = int(input())
# for i in range(k):
#     a = s[i]
#     l.append(a)
# new = " ".join(l)
# print(new)

# nums = list(map(int, input().split()))
# a = list(map(lambda x:x*x,nums))
# new = sorted(a)
# print(new)

# even = []
# odd = []
# nums = list(map(int, input().split()))
# for i in nums:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# ans_even = sorted(even)
# ans_odd = sorted(odd,reverse=True)
# ans = ans_even+ans_odd
# print(ans)

# l = []
# for i in range(6):
#     lst = list(map(int, input().split()))
#     l.append(lst)
# count = 0
# for j in range(len(l)-1):
#     if (sum(l[j])+2) == sum(l[j+1]):
#         count += 1
# if count == len(l)-1:
#     print('true')
# else:
#     print('false')

# l = []
# nums = list(map(int, input().split()))
# for i in nums:
#     a = len(str(i))
#     l.append(int(a))
# count = 0
# for i in l:
#     if i % 2 == 0:
#         count+=1
# print(count)

# l = []
# for i in range(6):
#     lst = list(map(int, input().split()))
#     l.append(lst)
# l1 = sorted(l)
# l3 = []
# for i in l1:
#     l3.append(i[0])
# l4 = []
# for i in range(len(l3)-1):
#     a = l3[i+1] - l3[i]
#     l4.append(a)
# ans = max(l4)
# print(ans)

# words = list(map(str, input().split()))
# x = input()
# l = set()
# for i in words:
#     for j in i:
#         if j == x:
#             l.add(words.index(i))
# ans = list(l)
# print(ans)

# word1 = list(map(str, input().split()))
# word2 = list(map(str, input().split()))
# l1  = "".join(word1)
# l2  = "".join(word2)
# if l1 == l2:
#     print('true')
# else:
#     print('false')


# text = input().split()
# print(text)
# brokenLetters = input()
# l = set()
# for j in brokenLetters:
#       pass
# for i in text:
#     if j not in i:
#         l.add(i)

# new = len(l)
# print(new)


# nums = list(map(int, input().split()))
# k = int(input())
# new_nums = sorted(nums)
# count = 0
# for i in new_nums:
#     if i<k:
#         nums.remove(i)
#         count += 1
# print(count)
            
# dictionary = list(map(str, input().split()))
# sentence = input()
# new_sentence = sentence.split()
# for i in range(len(new_sentence)):
#     for j in dictionary:
#         if new_sentence[i][0] == j[0]:
#             new_sentence[i] = j
#             break
# new_sentence = " ".join(new_sentence)
# print(new_sentence)

# nums1 = list(map(int, input().split()))
# nums2 = list(map(int, input().split()))
# k = int(input())
# nums3 = nums1+nums2
# sorted_nums3 = sorted(nums3)
# l = []
# for i in range(k):
#     a = sorted_nums3.pop()
#     l.append(a)
# print(l)

# count = False
# arr = list(map(int, input().split()))
# for i in range(len(arr)-2):
#     if arr[i]%2 != 0 and arr[i+1]%2 != 0 and arr[i+2]%2 != 0:
#         count = True
# if count == True:
#     print('true')
# else:
#     print('false')

l = set()
arr = list(map(int, input().split()))
for i in arr:
    if arr.count(i) > 1:
        l.add(i)
l1 = l.pop()
print(l1)