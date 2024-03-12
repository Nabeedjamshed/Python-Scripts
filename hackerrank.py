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

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
values = []
n1 = input().split()
for i in n1:
    n2 = i
    n3 = int(n2)
    values.append(n3)
my_dict = {k: v for k, v in zip(keys, values)}
string = input()
length = len(string)

l = []
for i in string:
    if i in my_dict:
        a = my_dict[i]
        l.append(a)
maximum = max(l)
final = length * maximum
print(final)