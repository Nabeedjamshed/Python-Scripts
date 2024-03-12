# match variable_name: syntax
#             case ‘pattern1’ : //statement1
#             case ‘pattern2’ : //statement2
#             …
#             case ‘pattern n’ : //statement n
# x = int(input("Enter the value of x: "))
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     case 1:
#         print("x is one")
#     case 2:
#         print("x is two")
#     case 3:
#         print("x is 3")
#     # case with if-condition
#     case 4:
#         print("case is 4")
#     case 5:
#         print("x is 5")
#
#     case _ if x!=90:
#         print(x, "is not 90")
#     case _ if x!=80:
#         print(x, "is not 80")
#     case _:
#         print(x)

num = int(input("Enter no: "))

match num:
    case 0:
        print("num is zero")
    case 1:
        print("num is one")
    case 4:
        print("num is 4")
    case _ if num >= 5 and num <= 10:
        print("num is lie between 5-10")
    case _ if num >= 11 and num <= 50:
        print("num is lie between 11- 50")
    case _ :
        print("num is greater than 50")
