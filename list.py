# l = [43,12,24,1,23,45,67]
# size = len(l)
# for i in range(0,size):
#     for j in range(0,size-1):
#         if l[j] > l[j+1]:
#             temp = l[j+1]
#             l[j+1] = l[j]
#             l[j] = temp
# print(l)

# def name(fname,mname,lname='Ali'):
#     print("Hello",fname,mname,lname)
# name('Nabeed','Jamshed')

## AVERAGE OF A NUMBERS!!!
# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum += i
#         average = sum/len(numbers)
#     print("The average is: ",average)
# average(5, 4, 3, 8)

# def average1(*numbers):
#     sum = 0
#     for i in numbers:
#         sum += i
#         average = sum/len(numbers)
#         return average
# c = average1(2,4,5,6)
# print(c)

# l = [1,3,5,7,'Nabeed',4,'Huma']
# print(l[-3]) #negative index
# # Convert negative index into positive
# print(l[len(l)-3])
# print(l[5-3])
# print(l[2]) #Positive  index
# if 'Nabeed' in l:
#     print("YES Nabeed is present")
# else:
#     print("NO Nabeed is absent")
#
# if 'Na' in 'Nabeed':
#     print("YES")\
# # List Slicing
# print(l)
# print(l[ : ]) # [0 : len(l)]
# print(l[1:])
# print(l[1:-1])
# print(l[1:6:2])

## LIST COMPREHENSION!!!
# l = [i for i in range(10)]
# print(l)
# l = [i*i for i in range(10)]
# print(l)
# l = [i*i for i in range(10) if i%2 == 0]
# print(l)
l = ['Nabeed','Jamshed','Huma','Filza','Sualiha']
namewith_e = [item for item in l if 'e' in item]
print(namewith_e)

l = ['Nabeed','Jamshed','Huma','Filza','Sualiha']
namewith_e = [item for item in l if (len(item) > 4)]
print(namewith_e)