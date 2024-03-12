# lst = []
# for i in range(100):
#     if i % 3 == 0:
#         lst.append(i)
# print(lst)

# LIST COMPREHENSION!!
# lst = [i for i in range(100) if i % 3 == 0]
# print(lst)

# Dictionary Comprehension!!
# dic = {i:f"item {i}" for i in range(1, 10001) if i % 100 == 0}
# print(dic)

# Reverse Key Value pair!!
# dic1 = {i:f'Item {i}' for i in range(5)}
# dic2 = {value:key for key, value in dic1.items()}
# print(dic1, '\n', dic2)

#Set Comprehension!!
# dresses = {i for i in ['dress 1', 'dress 2','dress 1', 'dress 2']}
# print(dresses)

# items={"shirt","pasta","biryani","iron","cold drink"}
# d1={}
# price_list=[]
# for i in range(len(items)):
#     x=items.pop()
#     print("Enter price for",x)
#     d1[x]=int(input())

# amount=0
# for j in d1.values():
#     price_list.append(j)
#     amount+=j

# print("*********BILL**********")
# print("{:<15}{:<15}".format("ITEMS","PRICE"))
# for a,b in d1.items():
#     print("{:<15}{:<15}".format(a,b))
# print("Total Amount= Rs.",amount)
# print("Maximun Price=",max(price_list))
# print("Minimum Price=",min(price_list))
# print("THANKS FOR VISITING")


# items = {'Ice-cream', 'Noodles', 'Biryani', 'Cold drink', 'Burger'}
# d = {}
# x = []
# for i in range(len(items)):
#     a = items.pop()
#     p_dishes = int(input(f"Enter the price of {a}: "))
#     x.append(p_dishes)
#     d[a] = p_dishes
# print(d)

# print('YOUR BIL!!')
# print('________________________________')
# print('ITEMS','\t\t\t','PRICE')
# print('________________________________')

# for j in d:
#     print(j,'\t\t\t',i,'\n')

# print(f'Total Amount = Rs. {sum(x)}','\n')
# print(f'Maximim Price = Rs. {max(x)}','\n')
# print(f'Minimum Price = Rs. {min(x)}','\n')
# print('____________________________________','\n')
# print('THANK YOU SO MUCH')


items = {'Ice-cream', 'Noodles', 'Biryani', 'Cold drink', 'Beef Burger'}
d = {}
x = []

for i in range(len(items)):
    a = items.pop()
    p_dishes = int(input(f"Enter the price of {a}: "))
    x.append(p_dishes)
    d[a] = p_dishes
    print(p_dishes)

print(d)

print('YOUR BILL!!')
print('___________________________________')
print('ITEMS', '\t\t\t', 'PRICE')
print('___________________________________')

for j in d:
    print(j, '\t\t\t', d[j],'\n')

print(f'Total Amount = Rs. {sum(x)}', '\n')
print(f'Maximum Price = Rs. {max(x)}', '\n')
print(f'Minimum Price = Rs. {min(x)}', '\n')
print('____________________________________', '\n')
print('THANK YOU SO MUCH')