# def crypto(file_name):
#     with open(file_name,'r') as f:
#         content = f.read()
#         r_content = content.replace('secret','xxxxxx')
#         print(r_content)
# crypto("crypto.txt")

# tickets =[2,3,2]
# k = 2
# counts = 0
# i = 0
# while tickets[k] != 0:
#     if tickets[i] != 0:
#         tickets[i] = tickets[i]-1
#         counts+=1
#         i += 1
#         if i == len(tickets):
#             i = 0
#     else:
#         i += 1
#         if i == len(tickets):
#             i = 0
# print(counts)


# arr = [1,2,3,5] 
# k = 3
# d1 = [] 
# d3 = []
# for i in range(len(arr)):
#     d2 = []
#     for j in range(i+1,len(arr)):
#         d1.append(arr[i] / arr[j])
#         d2.append(arr[i])
#         d2.append(arr[j])
#         d3.append(d2)
# print(d1)
# print(d3)

# arr = [1, 2, 3, 5]
# arr.sort()
# d1 = []
# d3 = []

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         d1.append((arr[i], arr[j]))  # Use tuple instead of list for keys
#         d3.append(arr[i] / arr[j])

# dic = dict(zip(d1, d3))
# print(d1)
# print(d3)
# print(dic)


# nums1 = [1,2,3]
# nums2 = [2,4,6]
# nums1 = set(nums1)
# nums2 = set(nums2)
# diff1 = list(nums1-nums2)
# diff1 = list(nums2-nums1)
# return [diff1, diff2]


# s = list("abbaca")
# i = 0
# while True:
#     if s[i]==s[i+1]:
#         s.pop(s[i])
#         s.pop(s[i+1])
#     i += 1

# pushed = [1, 2, 3, 4, 5]
# popped = [4, 5, 3, 2, 1]
# push = []
# for i in range(len(pushed)):
#     if pushed[i] != popped[i]:
#         push.append(i)
#     else:
#         push.pop()
# print(push)


# print("Marks Out of 10")
# l = []
# for i in range(1,11):
#     marks = int(input(f"Enter the marks of student {i}: "))
#     l.append(marks)
# avg = sum(l) / len(l)
# print(avg)


n = 12
m = 6
ans1 = n+m
print ("addition of" , n , "and" , m , "is" , ans1 )
ans2 = n-m
print ("subtraction of" , n , "and" , m , "is" , ans2 )
ans3 = n*m
print ("multiplication of" , n , "and" , m , "is" , ans3 )
ans4 = n/m
print ("division of" , n , "and" , m , "is" , ans4 )
ans5 = n**m
print ("exponantional of" , n , "and" , m , "is" , ans5) 
ans6 = n//m
print ("floor division of" , n , "and" , m , "is" , ans6)
ans7 = n%m
print (" modulus of" , n , "and" , m , "is" , ans7)
