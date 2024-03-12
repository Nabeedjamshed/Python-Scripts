# sample_list = [2, 1, 3, 5, 4, 3, 8]
# del sample_list[3:4]
# sample_list.remove(1)
# sample_list.sort()
# sample_list.insert(0, 1)
# sample_list.pop(2)
# sample_list.extend([10, 11, 12])
# print(sample_list)
#
# import math
#
#
# def height(length, d_angle):
#     r_angle = (math.pi * d_angle) / 180
#     height = length * math.sin(r_angle)
#     return height
#
#
# print(f"A ladder of 16 feet lenght and 75 degree angle, the height is "
#       f"{height(16, 75):.2f} feet.")
# print(f"A ladder of 20 feet lenght and 0 degree angle, the height is "
#       f"{height(20, 0):.2f} feet.")
# print(f"A ladder of 24 feet lenght and 45 degree angle, the height is "
#       f"{height(24, 45):.2f} feet.")
# print(f"A ladder of 24 feet lenght and 80 degree angle, the height is "
#       f"{height(24, 80):.2f} feet.")

lst = [6, 2, 8, 9, 10, 4, 3, 7, 1, 5, 12]
middle_index = len(lst) // 2
middle_element = lst[middle_index]
lst.sort(reverse=True)
print(f"The list in descending order is : {lst}")
lst.append(lst.pop(0))

print(f"The index of middle element is {middle_index}.")
print(f"The middle element of list is {middle_element}.")
print(f"List after remove 1st no and put it on Last: {lst}")

monthsL = ['Jan', 'Feb', 'Mar', 'May']
monthsT = ('Jan', 'Feb', 'Mar', 'May')

monthsL.insert(3, 'Apr')
# monthsT.insert(3,'Apr') Tuples are immutable

monthsL.append('Jun')
#  monthsT.append('Jun') Tuples are immutable

monthsL.pop()
#  monthsT.pop() Tuples are immutable

del monthsL[1]
#  del monthsT[1] Tuples are immutable

monthsL.reverse()
#  monthsT.reverse() Tuples are immutable

monthsL.sort()
#  monthsT.sort() Tuples are immutable

print('monthsL', monthsL)
print('monthsT', monthsT)

# a = 6
# b = 7
# c = (a + b) / 2
# inventory = ['Paper', 'Staples', 'Pencils']
# first = 'John'
# middle = 'Fitzgerald'
# last = 'Kennedy'
# fullname = first + ' ' + middle + ' ' + last
# print(fullname)