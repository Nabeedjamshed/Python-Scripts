# def sum(a,b):
#     return a+b
# print("The sum is",sum(9,2))
# print("The sum is",sum(2,8))
# print("The sum is",sum(8,5))
# print("The sum is",sum(9,6))

# no = int(input("Enter No: "))
# def facto(no):
#     if no == 0 or no == 1:
#         return 1
#     else:
#         fact = 1
#         for i in range(1,no+1):
#           fact = fact * i
#         return fact
# # print("The Factorial of",no,"is",facto(no))
# for i in range(0,11):
#     print(f"{i}! = {facto(i)}")

# a = 1
# for i  in range(11):
#     a += 1
#     print(i)

# tno = int(input("Enter Table No: "))
# limit = int(input("Enter Table Limit: "))
# def table(tno,limit):
#     for i in range(tno,limit+1):
#         print(tno,'*',i,'=',tno*i,table(i))


initial = int(input("Enter initial value: "))
final = int(input("Enter final value: "))
for i in range(initial,final+1):
    for j in range(initial,final+1):
        print(i*j,end="\t")
    print()