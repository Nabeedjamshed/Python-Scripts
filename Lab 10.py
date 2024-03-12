# Q : 1
# family = {
#     "Me": {"Name": "Nabeed", "Age": 18},
#     "Father": {"Name": "Jamshed", "Age": 43},
#     "Mother": {"Name": "Huma","Age":40},
#     "Siblings": [
#         {"Name": "Filza", "Age": 15},
#         {"Name": "Sualiha", "Age": 12}
#     ]
# }
#
# family.update({
#     "Maternal Grandfather": {"Name": "Ilyas", "Age": 75},
#     "Maternal Grandmother": {"Name": "Zaitoon", "Age": 70},
#     "Paternal Grandmother": {"Name": "Akhtari", "Age": 78}
# })
#
# family.update({
#     "Maternal Uncle": {"Name": "Imran", "Age": 45},
#     "Maternal Aunt": {"Name": "Farah", "Age": 42},
#     "Paternal Uncle": {"Name": "Anil", "Age": 55},
#     "Paternal Aunt": {"Name": "Heena", "Age": 50}
#     "Paternal Grandfather": {"Name": "Haji", "Age": 80},
# })
#
# print('\n'"Dynamic Family Directory!!",'\n')
# for i,j in family.items():
#     print(i)
#     if isinstance(j,list):
#         for sib in j:
#             for key, value in sib.items():
#                 print(f"\t{key} = {value}")
#     else:
#         for key, value in j.items():
#             print(f"\t{key} = {value}")
# Q : 5

# def count_guests(guest_list):
#     count = 0
#     for guest in guest_list:
#         if isinstance(guest, tuple):
#             count += len(guest)
#         else:
#             count += 1
#     return count
#
#
# def common_guests(list1, list2):
#     common = []
#     for guest in list1:
#         if guest in list2:
#             common.append(guest)
#     return common
#
#
# parents_list = ["Nabeed", "Talha", ("Kamran", "Ashan", "Ayan"), "Haris", "Anus"]
# my_list = ["Nabeed", "Talha", "Abyaz", "Awwab", ("Karim", "Hamza"), "Affan"]
# common_list = common_guests(parents_list, my_list)
#
# print("Number of guests in parents' list:", count_guests(parents_list))
# print("Number of guests in your list:", count_guests(my_list))
# print("Number of common guests:", count_guests(common_list))
#
# total_guests = count_guests(parents_list) + count_guests(my_list) - count_guests(common_list)
# print("Total number of guests:", total_guests)

# Q : 4
# your_choice = {"pizza": 5, "burger": 4, "salad": 3, "pasta": 4, "chicken": 3}
# cooked = {"Monday": "pizza", "Tuesday": "salad", "Wednesday": "pasta", "Thursday": "chicken", "Friday": "burger", "Saturday": "pizza", "Sunday": "pasta"}
# common_dishes = []
# for day, dish in cooked.items():
#     if dish in your_choice:
#         common_dishes.append(dish)
# print("Number of dishes that are both in your choice and cooked in a week:", len(common_dishes))
# print("Names of those dishes:", ", ".join(common_dishes))

# Q : 3
# def hexASCII():
#     for char in range(ord('a'), ord('z') + 1):
#         ascii_value = ord(chr(char))
#         hex_value = format(ascii_value, 'x')
#         print(chr(char) + ':' + hex_value)
#
#
# hexASCII()

# Q : 2
# def create_phone_directory():
#     phone_directory = {}
#     for i in range(12):
#         name = input("Enter the name of member " + str(i + 1) + ": ")
#         number = input("Enter the phone number of member " + str(i + 1) + ": ")
#         phone_directory[name] = number
#     return phone_directory

#
# def delete_member(phone_directory):
#     name = input("Enter the name of the member to delete: ")
#     if name in phone_directory:
#         del phone_directory[name]
#         print(name + " has been deleted from the phone directory.")
#     else:
#         print(name + " is not in the phone directory.")
#
#
# def print_total_members(phone_directory):
#     total_members = len(phone_directory)
#     print("Total number of members in the phone directory: " + str(total_members))
#
#
# phone_directory = create_phone_directory()
# delete_member(phone_directory)
# print_total_members(phone_directory)
