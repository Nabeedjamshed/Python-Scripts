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

# l = set()
# arr = list(map(int, input().split()))
# for i in arr:
#     if arr.count(i) > 1:
#         l.add(i)
# l1 = l.pop()
# print(l1)

# import math as m
# s = input()
# letter = input()
# counting = s.count(letter)
# length = int(len(s))
# result = m.floor(counting / length * 100)
# print(result)

# l = set()
# s = input()
# for i in s:
#     if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
#         l.add(int(i))

# if len(l) <= 1:
#     print(-1)
# else:
#     sorted_l = sorted(l)
#     ans = sorted_l[-2]
#     print(ans)

# words = list(map(str, input().split()))
# left = int(input())
# right = int(input())
# counts = 0
# vowels = ['a', 'e', 'i', 'o', 'u']
# for i in range(left, right+1):
#     for j in vowels:
#         if words[i] == j:
#             counts += 1
#         elif words[i][0] == j and words[i][-1] == j:
# print(counts)


# nums1 = list(map(int, input().split()))
# nums2 = list(map(int, input().split()))
# nums1_nums2 = nums1 + nums2
# s = set()
# for i in nums1:
#     if i in nums2:
#         s.add(i)
# l = []
# for i in s:
#     a = nums1_nums2.count(i)
#     l.append(a)
# if not l:
#     l.append(0)
#     l.append(0)
# new = sorted(l)
# print(new)

# s = input()
# s_upper = s.upper()
# l = set()
# for i in s_upper:
#     if s_upper.count(i) > 1:
#         l.add(i)
# lst = list(l)
# # print(lst)
# for j in lst:
#     if ord(j) >= 26 or ord(j) <= 1:
#         lst.remove(j)
# print(lst)
# if not lst or len(lst) == 1:
#     print("")
# else:
#     sorted_l = sorted(lst)
#     new = sorted_l[-1]
#     print(new)

# negative = []
# positive = []
# nums = list(map(int, input().split()))
# for i in nums:
#     if i<0:
#         negative.append(i)
#     else:
#         positive.append(i)
# negative_becomes_positive = []
# for j in negative:
#     negative_becomes_positive.append(abs(j))
# l = []
# for k in positive:
#     if k in negative_becomes_positive:
#         l.append(k)
#     else:
#         l.append(-1)
# if not l:
#     print(-1)
# else:
#     new = max(l)
#     print(new)

# def are_all_characters_present(str1, str2):
#     # Convert both strings to sets
#     set1 = set(str1)
#     set2 = set(str2)

#     # Check if set1 is a subset of set2
#     return set1.issubset(set2)

# # Example usage
# str1 = input()
# str2 = input()
# result = are_all_characters_present(str1, str2)
# print(result)  # Output: True


# str1 = input()
# str2 = input()
# set1 = set(str1)
# set2 = set(str2)
# print(set1)
# print(set2)
# print(set1.issubset(set2))


# from collections import Counter

# str1 = input()
# str2 = input()
# counter1 = Counter(str1)
# counter2 = Counter(str2)
# for char, counts in counter1.items():
#     if counter2[char] < counts:
#         print('false')
#         break
#     else:
#         print('true')
#         break


# l = list(map(int, input().split()))
# minimum = min(l)
# index = l.index(minimum)
# for i in range(index+1):
#     l.pop(0)
# if not l:
#     print(0)
# else:
#     maximum = max(l)
#     result = maximum-minimum
#     print(result)

# n = int(input())
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# new = str(fact)
# result = new.rstrip('0')
# new1 = len(new) - len(result)
# print(type(new1))


# n = int(input())
# new = bin(n)[2:]
# l = []
# for i in range(len(new)):
#     if new[i] == '1':
#         l.append(new[i])
# result = len(l)
# print(result)

# n = int(input())
# n_str = str(n)
# reverse = n_str[::-1]
# decimal = int(reverse,2)
# print(decimal)

# nums = list(map(int,input().split()))
# k = int(input())
# new = k-1
# sort = sorted(nums,reverse=True)
# result = sort[new]
# print(result)


# nums = list(map(int,input().split()))
# for j in range(5):
#     nums.append(0)
# l = []
# for i in range(5):
#     if i >= nums[i] and i :
#         l.append(i)
# print(l)


# def specialArray(nums):
#     n = len(nums)
#     for j in range(1, n + 1):
#         counts = 0
#         for i in nums:
#             if i>=j:
#                 counts += 1
#         if counts == j:
#             return j
#     return -1
# nums = list(map(int,input().split()))
# a = specialArray(nums)
# print(a)


# nums = list(map(int, input().split()))
# target = int(input())
# l = []
# for i in nums:
#     if i == target and nums.index(i) not in l:
#         l.append(nums.index(i))
# if not l:
#     l.append(-1)
# # a = l.pop()
# print(l)


# nums = list(map(int, input().split()))
# sorted_nums = sorted(nums)
# if len(sorted_nums) == 1 or len(sorted_nums) == 2:
#     print(1)
# else:
#     l = set()
#     for i in range(len(sorted_nums)-1):
#         if (sorted_nums[i+1] - sorted_nums[i]) == 1:
#             l.add(sorted_nums[i])
#             l.add(sorted_nums[i+1])
#     new = len(l)
#     print(new)

# nums = list(map(int, input().split()))
# val = int(input())
# new_nums = []
# for i in nums:
#     if i != val:
#         new_nums.append(i)
# c = len(nums) - len(new_nums)
# print(len(new_nums))
# new_nums.extend("_" * c)
# print(new_nums)


# nums = list(map(int, input().split()))
# if len(nums) == 1:
#     print(nums[0])
# else:
#     for i in range(len(nums)-1):
#         if nums.count(nums[i]) <= nums.count(nums[i+1]):
#             print(nums[i+1])
           
#     else:
#         print(nums[i])

# nums = list(map(str, input().split()))
# k = int(input())
# l = []
# for i in nums:
#     if nums.count(i) == 1:
#         l.append(i)
# if len(l) < k:
#     print("")
# else:
#     new = l[k-1]
#     print(new)

# nums = list(map(str, input().split()))
# s = input()
# l = []
# for i in nums:
#     words = i[0]
#     l.append(words)
# a = "".join(l)
# if a == s:
#     print('true')
# else:
#     print('false')

# s = input()
# t = input()
# maxCost = int(input())
# l = []
# for i in range(len(s)):
#     a = abs(ord(s[i]) - ord(t[i]))
#     l.append(a)
# print(l)

# numbers = list(map(str, input().split()))
# l = []
# for i in numbers:
#     l.append(len(i))
# a = max(l)
# print(a)


# sentences = ["please wait", "continue to fight", "continue to win"]
# l = []
# for i in sentences:
#     a = i.split()
#     l.append(a)
# l2 = []
# for j in l:
#     b = len(j)
#     l2.append(b)
# x = max(l2)
# print(x)


# s = input()
# integer = int(s,2)
# print(integer)
# counts = 0
# while(integer > 1):
#     if integer % 2 == 0:
#         integer = int(integer // 2)
#         counts += 1
#     else:
#         integer = int(integer+1)
#         counts += 1
# print(counts)



# nums = list(map(int, input().split()))
# target = int(input())
# l = []
# for i in range(len(nums)):
#     if nums[i] == target:
#         l.append(i)
# if not l:
#     l.append(-1)
#     l.append(-1)
# if len(l) != 2:
#     l.append(0)
# print(l)


# nums = list(map(int, input().split()))
# my_dict = {}
# for i in nums:
#     if i in my_dict:
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1
# a = max(my_dict.values())
# l = []
# for x,y in my_dict.items():
#     if y == a:
#         l.append(x)
# sorted_l = sorted(l)
# print(sorted_l)



# s = input()
# wordDict = list(map(str, input().split()))
# counts = 0
# for i in wordDict:
#     if i in s:
#         counts += 1
# if counts == len(wordDict):
#     print('true')
# else:
#     print('false')

# a = int(input())
# b = int(input())
# l = []
# for i in range(a):
#     l.append('a')
# for i in range(b):
#     l.append('b')
# result = "".join(l)

# print(result)

# matrix = [[1,2],[1,3]]
# k = int(input())
# l = []
# for i in matrix:
#     for j in i:
#         l.append(j)
# sorted_l = sorted(l)
# result = sorted_l[k-1]
# print(result)

# nums = list(map(int, input().split()))
# my_dict = {}
# for i in nums:
#     if i in my_dict:
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1
# a = max(my_dict.values())
# if a == 1:
#     nums.clear()
#     print(nums)
# else:
#     l = []
#     for x,y in my_dict.items():
#         if y == a:
#             l.append(x)
#     if len(nums) <= 1:
#         nums.pop(0)
#         print(nums)
#     else:
#         sorted_l = sorted(l)
#         print(sorted_l)


# nums = list(map(int, input().split()))
# target = int(input())
# mid = len(nums) // 2
# right = nums[:mid]
# left = nums[mid:]
# print(right)
# print(left)

# def first(nums, target):
#     left = 0
#     right = len(nums)-1
#     while left<=right:
#         mid = (left+right) // 2
#         if target == nums[mid]:
#             return mid
#         elif target > nums[mid]:
#             left = mid+1
#         else:
#             right = mid-1
#     return -1

# nums = list(map(int, input().split()))
# target = int(input())
# a = first(nums,target)
# print(a)

# def binary_search(nums, target):
#     left, right = 0, len(nums) - 1  
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid  # Target found, return the index
#         elif nums[mid] < target:
#             left = mid + 1  # Search in the right half
#         else:
#             right = mid - 1  # Search in the left half
#     return -1  # Target not found

# def findLast(nums, target):
#     left, right = 0, len(nums) - 1
#     last_pos = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             last_pos = mid
#             left = mid + 1  # continue searching in the right half
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return last_pos

# nums = list(map(int, input().split()))
# target = int(input())

# result = binary_search(nums, target)
# result2 = findLast(nums,target)
# a = [result,result2]
# print(a)


# def searchRange(nums, target):
#     def findFirst(nums, target):
#         left, right = 0, len(nums) - 1
#         first_pos = -1
#         if target not in nums:
#             return first_pos
#         else:
#             while left <= right:
#                 mid = (left + right) // 2
#                 if nums[mid] == target:
#                     first_pos = mid
#                     right = mid - 1 
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return first_pos

#     def findLast(nums, target):
#         left, right = 0, len(nums) - 1
#         last_pos = -1
#         if target not in nums:
#             return last_pos
#         else:
#             while left <= right:
#                 mid = (left + right) // 2
#                 if nums[mid] == target:
#                     last_pos = mid
#                     left = mid + 1
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return last_pos

#     first_pos = findFirst(nums, target)
#     last_pos = findLast(nums, target)

#     return [first_pos, last_pos]
# nums = list(map(int, input().split()))
# target = int(input())
# print(searchRange(nums, target))

# nums = list(map(int, input().split()))
# queries = list(map(int, input().split()))
# x = int(input())
# l = []
# for i in range(0, len(nums)):
#     if nums[i] == x:
#         l.append(i)
#     else:
#         l.append(-1)

# if x not in nums:
#     l.clear()
#     for i in range(len(queries)):
#         l.append(-1)
# print(l)


# image = [[1,1,0],[1,0,1],[0,0,0]]
# new = []
# for i in image:
#     l = []
#     new_image = i[::-1]
#     for j in new_image:
#         if j == 0:
#             j = 1
#             l.append(j)
#         else:
#             j = 0
#             l.append(j)
#     new.append(l)
# print(new)


# nums = list(map(int, input().split()))
# target = int(input())
# first = -1
# for i in range(len(nums)):
#     if nums[i]==target:
#         first = i
#         break
# last = -1
# for j in range(-1, -len(nums)-1, -1):
#     if nums[j]==target:
#         a = len(nums)+j
#         last = a
#         break
# l = [first,last]
# print(l)


# deck = list(map(int, input().split()))
# l = []
# for i in range(len(deck)):
#     minimum = min(deck)
#     maximum = max(deck)
#     l.append(minimum)
#     l.append(maximum)
#     deck.remove(minimum)
#     deck.remove(maximum)
# print(l)


# arr = list(map(int, input().split()))
# percentage = int((len(arr) / 100) * 5)
# l = []
# for i in range(percentage):
#     maximum = max(arr)
#     minimum = min(arr)
#     l.append(maximum)
#     l.append(minimum)
#     arr.remove(maximum)
#     arr.remove(minimum)
# new = (sum(l)/len(l))
# print(new)


# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         self.counts = 0
#         for i in nums:
#             if i == target:
#                 self.counts += 1
#                 break
#         if self.counts == 1:
#             return True
#         else:
#             return False


# nums1 = list(map(int, input().split()))
# m = int(input())
# nums2 = list(map(int, input().split()))
# n = int(input())
# for i in range(n):
#     nums1[m+i] = nums2[i]
# nums1.sort()
# print(nums1)    

# s = input()
# d = {}
# for i in range(len(s)):
#     a = s.count(s[i])
#     d[s[i]] = a
# b = max(d.values())
# l = []
# for x,y in d.items():
#     if y == a:
#         l.append(x)
# result = "".join(l)
# print(result)

# grid = [[3,2],[1,0]]
# l = []
# for i in grid:
#     for j in i:
#         l.append(j)
# counts = 0
# for k in l:
#     if k<0:
#         counts += 1
# print(counts)    

# nums = list(map(int, input().split()))
# first = 0
# last = len(nums)-1
# mid = int((first + last) / 2)  
# new = nums[mid]
# new = nums[-1:-4:-1]
# for i in nums[-1:-4:-1]:
#     nums.remove(i)
# sorted_new = sorted(new,reverse=True)
# for j in sorted_new:
#     nums.append(j)

# print(nums)


# nums = list(map(int, input().split()))
# square = lambda x: x*2
# new_nums = []
# for i in nums:
#     if i == 0:
#         nums.remove(i)
#     else:
#         new_nums.append(square(i))
# for j in nums:
#     if j in new_nums:
#         print('true')
#         break
# else:
#     print('false')

# s = input()
# t = input()
# counts = 0
# for i in s:
#     if counts<len(t) and i == t[counts]:
#         counts += 1
# result = len(t) - counts
# print(result)

# import random as rd
# s = input()
# d = {}
# for i in range(len(s)):
#     a = s.count(s[i])
#     d[s[i]] = a
# l = []
# l2 = []
# for x,y in d.items():
#     if y%2 == 0:
#         divide = y//2
#         for i in range(divide):
#             l.append(x)
#             l.insert(0,x)
#     else:
#         if y == 1:
#             l2.append(x)
#             mid = int(len(s)//2)
#             if l2[0] not in l:
#                 l.insert(mid,l2[0])
#         else:
#             y = y-1
#             divide = int(y/2)
#             print(divide)
#             for i in range(divide+1):
#                 l.append(x)
#                 l.insert(0,x)   
# new = "".join(l)
# if len(new) % 2 == 0:
#     new = new[:-1]
#     result = len(new)
#     print(result)
# else:
#     result = len(new)
#     print(result)


# nums = list(map(int, input().split()))
# k = int(input())
# for i in range(k):
#     a = nums.pop()
#     nums.insert(0,a)
# print(nums)



# s = input()
# char_count = {} 
# for char in s:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# max_length = 0
# for i in char_count.values():
#     max_length += i // 2 * 2
# if max_length < len(s):
#     max_length += 1
# print(max_length)



# words = ["cool","lock","cook"]
# d = {}
# d1 = {}
# for i in words:
#     for j in range(len(i)):
#         a = i.count(i[j]) 
#         d[i[j]] = a
# for x,y in d.items():
#     if x in words[-1] and x in words[-2]:
#         d1[x] = y
# l = []
# print(d1)
# for a,b in d1.items():
#     new = b*a
#     l.append(new)
# result = "".join(l)
# final_result = list(result)
# print(final_result)


# words = ["cool","lock","cook"]
# l = []
# for i in range(len(words)-1):
#     a = set(words[i]).intersection(set(words[i+1]))
#     l.append(a)
# common = set(l[0]).intersection(set(l[1]))
# d = {}
# l1 = []
# for word in words:
#     for char in word:
#         char_counts = word.count(char)
#         l1.append(char_counts)
#         char_count = min(l1)
#         if char_count not in d and char in common:
#             d[char_count] = char

# l = []
# for a,b in d.items():
#     new = b*a
#     l.append(new)
# result = "".join(l)
# final_result = list(result)
# print(final_result)



# Algo 1
# hand = list(map(int, input().split()))
# sorted_hand = sorted(hand)
# groupSize = int(input())
# l = []
# if len(hand) % groupSize != 0:  
#     print('false')
# else:
#     for i in range(groupSize):
#         a = sorted_hand[0:groupSize:1]
#         l.append(a)
#         sorted_hand = sorted_hand[groupSize:]  
#     l1 = []
#     for j in l:
#         if j:
#             l1.append(j)
#     check = True
#     for k in l1:
#         if len(k) != groupSize:
#             check = False
#             break
#         for i in range(1, groupSize-1):
#             if len(l) != len(l1):
#                 check = False
#                 break
#     if check:
#         print('true')
#     else:
#         print('false')

# nums = list(map(int, input().split()))
# k = int(input())
# l = []
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if (nums[i] + nums[j]) % k == 0:
#             l.append(nums[i])
#             l.append(nums[j])
# print(l)
# l2 = []
# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if (l[i] + l[j]) == k:
#             l2.append(l[i])
#             l2.append(l[j])
# print(l2)
# if sum(l) % k == 0:
#     print(True)
# else:
#     print(False)


# answerkey = input()
# l = []
# for j in answerkey:
#     l.append(j)
# k = int(input())
# for i in range(k):
#     if l[i] == "T":
#         l[i] = "F"
# print(l)
# l2 = []
# for k in l:
#     if k == "T":
#         l2.append(k)
# result = len(l2)
# print(result)


# nums = list(map(int, input().split()))
# target = int(input())
# left = 0
# rigth = len(nums)-1
# mid = (left + rigth) // 2
# while left < rigth:
#     if target == nums[mid]:
#         mid = nums[mid]
#     elif target < nums[mid]:
#         mid = mid - 1
#     else:
#         mid = mid + 1
# print(mid)

# nums = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# target = int(input())
# flag = 0
# for i in nums:
#     for j in i:
#         if j == target:
#             flag = 1
# if flag == 1:
#     print(True)
# else:
#     print(False)


# dictionary = ["cat","bat","rat"]
# sentence = "the cattle was rattled by the battery"
# l = []
# for i in sentence:
#     if i in dictionary:
#         # sentence = sentence.replace(i)
#         l.append(True)
# print(l)


# nums = list(map(int, input().split()))
# k = int(input())
# add = sum(nums)
# divide = add % k
# if divide == 0:
#     print(True)
# else:
#     print(False)

# a = 41
# b = 7
# c = a // b
# print(c)


# arr = [5]
# k = int(input())
# subarrays = []
# for i in range(len(arr)):
#   for j in range(i, len(arr)):
#     subarrays.append(arr[i:j+1])
# l = []
# for j in subarrays:
#   l.append(sum(j))
# l1 = []
# for x in l:
#   if x%k == 0:
#     l1.append(x)
# result = len(l1)
# print(result)


# seats = list(map(int, input().split()))
# students = list(map(int, input().split()))
# sorted_seats = sorted(seats)
# sorted_students = sorted(students)
# l = []
# for i in range(len(seats)):
#     l.append(abs(sorted_seats[i] - sorted_students[i]))
# print(l)
# print(sum(l))

# def silding_window(s,p):
#     check = []
#     maximum = s[:len(p)]
#     total = maximum
#     sorted_max = sorted(maximum)
#     for i in range(len(s)-len(p)):
#         if sorted_max == p:
#             check.append(sorted_max[0])
#         else:
#             total -= s[i]
#             total += s[i+len(p)]
#     return check
# s = "cbaebabacd"
# p = "abc"
# a = silding_window(s,p)
# print(a)


# def sliding_window(s, p):
#     check = []
#     p_sorted = sorted(p)
#     window_length = len(p)
    
#     for i in range(len(s) - window_length + 1):
#         window = s[i:i + window_length]
#         if sorted(window) == p_sorted:
#             check.append(i)
    
#     return check

# s = "abab" 
# p = "ab"    
# a = sliding_window(s, p)
# print(a)


# cardPoints = [9,7,7,9,7,7,9] 
# k = 7
# first = cardPoints[:k]
# last = cardPoints[-1:-k-1:-1]
# first_sum = sum(first)
# last_sum = sum(last)
# if first_sum>last_sum:
#     print(first_sum)
# else:
#     print(last_sum)

# def sliding_window(cardPoints, k):
#     super_total = sum(cardPoints)
#     total = sum(cardPoints[:k])
#     min_total = total
#     for i in range(len(cardPoints) - k):
#         total -= cardPoints[i]
#         total += cardPoints[i+k]
#         min_total = min(min_total,total)
#     result = super_total-min_total
#     return result
# cardPoints = [100,40,17,9,73,75] 
# k = 3
# a = sliding_window(cardPoints,k)
# print(a)



# t = input()
# s = sorted(set(t))
# subarray = []
# n = len(t)
# for i in range(1,1 << n):
#     sub = ""
#     for j in range(n):
#         if i & (1 << j) != 0:
#             sub += t[j]
#     subarray.append(sorted(sub))
# new = "".join(s)
# l = []
# for j in subarray:
#     a = "".join(j)
#     l.append(a)
# l1 = []
# for k in l:
#     if new in k:
#         l1.append(k)

# print(l1)
# l = []
# for i in subarray:
#     if new in i:
#         l.append(i)
# print(l)
# newl = set(l)
# print(len(newl))


# nums = list(map(int, input().split()))
# k = int(input())
# l = []
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         a = abs(nums[i]-nums[j])
#         l.append(a)
# l.sort()
# result = l[k-1]
# print(result)

# nums = list(map(int, input().split()))
# maxi = max(nums)
# l = []
# for i in range(1,maxi+2):
#     l.append(i)
# s = set(nums)
# l1 = []
# for j in l:
#     if j not in s:
#         l1.append(j)
# print(len(l1))


# nums = list(map(int, input().split()))
# sorted_nums = sorted(nums)
# counts = 0
# l = []
# for i in sorted_nums:
#     if i not in l:
#         l.append(i)
#     else:
#         i +=1
#         if i not in l:
#             l.append(i)
#         else:
#             i += 1
#             l.append(i)
#         counts+=1
# print(sorted_nums)
# print(l)
# new = []
# for j in range(len(l)):
#     a = abs(sorted_nums[j] - l[j])
#     new.append(a)
# print(sum(new))


# nums = list(map(int, input().split()))
# sorted_nums = sorted(nums)
# counts = 0
# l = []
# for i in sorted_nums:
#     while i in l:
#         i += 1
#     l.append(i)

# new = []
# for j in range(len(l)):
#     a = abs(sorted_nums[j] - l[j])
#     new.append(a)
# print(sum(new))



# class Solution:
#     def minIncrementForUnique(self, nums: List[int]) -> int:
#         nums.sort()
#         moves = 0
#         for i in range(1, len(nums)):
#             if nums[i] <= nums[i - 1]:
#                 increment = nums[i - 1] - nums[i] + 1
#                 nums[i] += increment
#                 moves += increment
#         return moves

# nums = list(map(int, input().split()))
# k = int(input())
# subarray = []
# n = len(nums)
# for i in range(1,1 << n):
#     sub = []
#     for j in range(n):
#         if i & (1 << j) != 0:
#             su    b.append(nums[j])
#     subarray.append(sorted(sub))
# newsubarray = []
# for i in subarray:
#     if len(i) > k:
#         newsubarray.append(i)
# l = []
# print(newsubarray)
# for i in newsubarray:
#     odd_count = sum(1 for num in i if num % 2 != 0)
#     l.append(odd_count)

# print(l)


# w = 0 
# profits = [1,2,3]
# capital = [0,1,2]
# for i in range(len(capital)):
#     if capital[i] == w:
#         w += profits[i]
# print(w)


# nums = [1,2,3,4,3]
# l = []
# for i in nums:
#     if i+1 not in nums:
#         l.append(-1)
#     else:
#         l.append(i+1)
# print(l)

# nums = list(map(int, input().split()))
# k = int(input())
# l = []
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         a = abs(nums[i] - nums[j])
#         if a == k:
#             l.append(a)
# print(len(l))


# words = ["def","ghi"]
# newwords = []
# for i in words:
#     newwords.append(i[::-1])
# l = ""
# for j in range(len(words)):
#     if words[j] == newwords[j]:
#         l += newwords[j]
#         break
# print(l)

# arr = [0,0]
# check = 0
# for i in arr:
#     i = i*2
#     if i in arr:
#         check +=1
#         break
# if check == 1:
#     print(True)
# else:
#     print(False)


# nums = list(map(int, input().split()))
# goal = int(input())
# subarray = []
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         subarray.append(sum(nums[i:j+1]))
# check = 0
# for k in subarray:
#     if k == goals:
#         check += 1
# print(check)
# subarrays = []
# for i in range(len(nums)):
#     subarrays += [sum(nums[i:j]) for j in range(i+1, len(nums)+1)]
# check = 0
# for k in subarrays:
#     if k == goal:
#         check += 1
# print(check)


# distance = list(map(int, input().split()))
# new_distance = [None] + distance
# start = int(input())
# destination = int(input())
# first = new_distance[1:destination+1]
# sum_first = sum(first)
# for i in first:
#     distance.remove(i)
# second = sum(distance)

# if sum_first<second:
#     print(sum_first)
# else:
#     print(second)

# nums = list(map(int, input().split()))
# n = int(input())
# l = []
# for i in range(1,n+1):
#     l.append(i)
# subarray = []
# counts = 0
# while len(l) != len(subarray):
#     for k in range(len(nums)):
#         for j in range(k,len(nums)):
#             subarray.append(sum(nums[k:j+1]))
#     subarray.sort()
#     for x in range(1,n+1):
#         if l != subarray:
#             if x not in nums:
#                 nums.append(x)
#                 break
#     counts += 1
# print(counts)


# nums = list(map(int, input().split()))
# n = int(input())

# patches = 0
# reach = 0
# i = 0

# while reach < n:
#     if i < len(nums) and nums[i] <= reach + 1:
#         reach += nums[i]
#         i += 1
#     else:
#         reach += reach + 1
#         patches += 1

# print(patches)

# import math as m
# c = int(input())
# sq = int(m.sqrt(c))
# check = 0
# l = []
# for i in range(sq+1):
#     l.append(i)
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if (l[i] ** 2) + (l[j] ** 2) == c:
#             check += 1
#             break

# if check == 1:
#     print(True)
# else:
#     print(False)

# for i in range(sq+1):
#     a_sq = (i ** 2)
#     b_sq = c - a_sq
#     b_sqrt = m.sqrt(b_sq)
#     if b_sqrt.is_integer():
#         check += 1
#         break

# if check == 1:
#     print(True)
# else:
#     print(False)

# nums = [1,2,3,4,5]
# d = {}
# for i in range(len(nums)):
#     a = nums.count(nums[i])
#     d[nums[i]] = a
# l = []
# for x,y in d.items():
#     if y<2:
#         l.append(x)
# print(sum(l))

# nums = [2,2,1,1,1,2,2]
# d = {}
# for i in nums:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# maximum = max(d.values())
# for x,y in d.items():
#     if y == maximum:
#         print(x)


# nums = [1,1,1,2,2,3]
# k = int(input())
# for i in range(k):


# nums = [1]
# d = {}
# for i in nums:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# l = []
# for j in range(k):
#     maxi = max(d.values())
#     for x,y in d.items():
#         if y == maxi:
#             l.append(x)
#     d = {k: v for k, v in d.items() if v != maxi}
# print(l)


# nums = [23,2,6,4,7]
# k = 13
# l = []
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         a = nums[i:j+1]
#         if len(a) == 2:
#             l.append(a)
# check = 0
# for j in l:
#     add = sum(j)
#     if add % k == 0:
#         check += 1
#         break
# if check == 1:
#     print(True)
# else:
#     print(False)


# nums = [1,2,3,3,2,1]
# d = {}
# for i in nums:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# l = []
# for x,y in d.items():
#     if y > 1:
#         l.append(x)
# if not l:
#     print(0)
# elif len(l) == 1:
#     print(l[0])
# else:
#     check = l[0]
#     for i in range(1,len(l)):
#         check = check ^ l[i] 
#     print(check)


# difficulty = [2,4,6,8,10]
# profit = [10,20,30,40,50]
# worker = [4,5,6,7]
# d = {}
# sorted_worker = sorted(worker)
# for i in range(len(worker)):
#     if worker[i] in difficulty:
#         a = difficulty.index(worker[i])
#         d[worker[i]] = a
#     else:
#         a = difficulty.index(worker[i-1])
#         d[worker[i]] = a

# print(d)
# difficulty = [2,4,6,8,10]
# profit = [10,20,30,40,50]
# worker = [4,5,6,7]
# l = []
# jobs = dict(zip(difficulty, profit))
# for x,y in jobs.items():
#     if x in worker:
#         l.append(y)
#     else:
#         for i in range(len(worker)):
#             if x-i in jobs.keys():
#                 l.append(y)

# print(l)

# difficulty = [66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63]
# profit = [66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77]
# worker = [61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]
# l = []
# d = dict(zip(difficulty, profit))
# for i in worker:
#     max_profit = 0
#     for x, y in d.items():
#         if x <= i and y > max_profit:
#             max_profit = y
#     l.append(max_profit)
# print(sum(l))

# difficulty = [85,47,57]
# profit = [24,66,99]
# worker = [40,25,25]
# d = dict(zip(difficulty, profit))
# l = []
# for i in range(len(worker)):
#     if worker[i] in d:
#         l.append(d[worker[i]])
#     else:
#         worker[i] = worker[i-1]
#         l.append(d[worker[i]])
# print(sum(l))


# def maxProfitAssignmentSimple(difficulty, profit, worker):
#   d = list(zip(difficulty, profit))
#   d.sort(key=lambda x: x[1], reverse=True)
#   max_profit = 0
#   for i in worker:
#     for x, y in d:
#       if x <= i:
#         max_profit += y
#         break  
#   return max_profit


# bloomDay = list(map(int, input().split()))
# m = int(input())
# k = int(input())

# # if (m * k) > len(bloomDay):
# #     print(-1)
# # else:
# #     l = []
# #     for i in range(m):
# #         for j in range(k):
# #             l.append(bloomDay[i * k + j])

# #     print(max(l))


# g = list(map(int,input().split()))
# s = list(map(int,input().split()))
# # s_set = set(s)
# counts = 0
# # for i in s_set:
# #     if i in g:
# #         counts +=1
# # print(counts)
# for i in g:
#     for j in s:
#         if s[i] >= g[j]:
#             counts+=1
# print(counts)



# nums = [1,1]
# s1 = set(sorted(nums))
# n = len(nums)
# s2 = set()
# for i in range(1,n+1):
#     s2.add(i)
# new = list(s1 ^ s2)
# print(new)

# nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# maxi = 0
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         add = nums[i] ^ nums[j]
#         if add > maxi:
#             maxi = add
# print(maxi)


# arr = [1,2,3]
# l = []
# for i in arr:
#     if len(l) > len(arr):
#         break
#     else:  
#         if i == 0:
#             l.append(0)
#             l.append(0)
#         else:
#             l.append(i)
# print(l)

# arr = [10,11,12]
# l = []
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         a = arr[i:j+1]
#         if len(a) % 2 != 0:
#             l.append(sum(a))
# print(sum(l))

# mat = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
# l = []
# for i in range(len(mat)):
#     for j in range(len(mat)):
#         if i == j:
#             l.append(mat[i][j])
#         elif i == len(mat)-j-1:
#             l.append(mat[i][j])
# print(sum(l))

# def mult(arr):
#     mul = 1
#     for i in arr:
#         mul = mul * i
#     return mul
# nums = list(map(int,input().split()))
# l = []
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         l.append(nums[i:j+1])
# l1 = []
# for k in l:
#     m = mult(k)
#     if m > 0:
#         l1.append(len(k))
# print(max(l1))


# arr = [2,3,4,7,11]
# k =int(input())
# s1 = set(arr)
# s2 = set()
# for i in range(1,100):
#     s2.add(i)
# s3 = list(s2-s1)
# new = s3[k-1]
# print(new)

# import math as m
# nums = [[1,2,3],[5,17,7],[9,11,10]]
# l = []
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i == j or i == len(nums) - j - 1:
#             l.append(nums[i][j])
# l1 = []
# for number in l:
#     if number <= 1:
#         continue
#     is_prime = True
#     for j in range(2, int(m.sqrt(number)) + 1):
#         if number % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         l1.append(number)
# if l1:
#     return max(l1)
# else:
#     return 0


import math as m
# n = int(input())
# l = []
# for number in range(n):
#     if number <= 1:
#         continue
#     is_prime = True
#     for j in range(2, int(m.sqrt(number)) + 1):
#         if number % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         l.append(number)
# if l:
#     print(len(l))
# else:
#     print(0)


# import math
# n = int(input())
# l1 = 0
# for num in range(n):
#     if num <= 1:
#         continue 
#     if num == 2:
#         l1 += 1
#         continue 
#     if num % 2 == 0:
#         continue  
#     is_prime = True
#     for i in range(3, int(math.sqrt(num)) + 1, 2):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         l1+=1
# print(l1)


# n = int(input())
# for i in range(1,(n*2)+1):
#     if (i % n == 0) and (i%2 == 0):
#         print(i)
#         break

# a = int(input())
# b = int(input())
# s1 = set()
# for i in range(1,a+1):
#     if a%i == 0:
#         s1.add(i)
# s2 = set()
# for i in range(1,b+1):
#     if b%i == 0:
#         s2.add(i)
# s3 = s1.intersection(s2)
# print(len(s3))

    # if n % 2 == 0:
    #     return False  
    # is_prime = True
    # for i in range(3, int(math.sqrt(n)) + 1, 2):
    #     if n % i == 0:
    #         is_prime = False
    #         break
    # return is_prime

# def palig(n):
#     n_str = str(n)
#     reverse_n = n_str[::-1]
#     if n_str == reverse_n:
#         return True
#     else:
#         return False
# def prime(n):
#     if n <= 1:
#         return False 
#     elif n == 2:
#         return True
#     else:
#         p = [0] * (n + 1)
#         for i in range(2, n + 1):
#             if p[i] == 0:
#                 for j in range(i*i, n+1, i):
#                     p[j] = 1
#         return p[n] == 0
# n = int(input())
# i = n
# while True:
#     a = palig(i)
#     b = prime(i)
#     if a == True and b == True:
#         print(i)
#         break
#     else:
#         i += 1

# customers = [1,0,1,2,1,1,7,5]
# grumpy = [0,1,0,1,0,1,0,1]
# minutes = 3
# d = list(zip(grumpy,customers))
# initial = []
# for x,y in d:
#     if x == 0:
#         initial.append(y)
# print(initial)
# def sliding_window(initial,minutes):
#     minutes = minutes-1
#     total = sum(initial[:minutes])
#     maxtotal = total
#     for i in range(len(initial)-minutes):
#         total -= initial[i]
#         total += initial[i+minutes]
#         maxtotal = max(maxtotal,total)
#     return maxtotal

# final = sliding_window(customers,minutes)
# print(final)


# nums = list(map(int, input().split()))
# a = max(nums)
# b = min(nums)
# while(b!=0):
#     temp = b
#     b = a%b
#     a = temp
# print(a)

# nums = [1,1,1,1,1]
# k = 1
# l = []
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         l.append(nums[i:j+1])
# print(l)
# subarray = []
# for i in l:
#     sub = []
#     for j in i:
#         if j%2 != 0:
#             sub.append(True)
#     subarray.append(len(sub))
# increment = 0
# for i in subarray:
#     if i == k:
#         increment +=1
# print(increment)

# def gcd(t):
#     a = max(t)
#     b = min(t)
#     while(b!=0):
#         temp = b
#         b = a%b
#         a = temp
#     return a
# nums = [1,2,3,4,5,6]
# l = []
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         l.append((nums[i],nums[j]))
# l1 = []
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         g = gcd(l[i]) + gcd(l[j])
#         l1.append(g)
# # for i in range(1,int(len(nums)/2)+1):

# print(l1)