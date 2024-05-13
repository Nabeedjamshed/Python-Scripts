# rows = int(input("Enter a number of rows: "))
# columns = int(input("Enter a number of columns: "))
# l = []
# for i in range(rows):
#     k = []
#     for j in range(columns):
#         n = int(input(f"You are entering a data for {i+1} row and {j+1} columns: "))
#         k.append(n)
#     l.append(k)
# for j in l:
#     print(j)

# days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# province_list = []
# province_temperature = []
# average = []
# for i in range(4):
#     province = input("Enter a name of a province: ")
#     province_list.append(province)
#     province_temp = []
#     for j in days:
#         temp = int(input(f"Enter a temperature of {j}: "))
#         province_temp.append(temp)
#         add = sum(province_temp)
#         length = len(province_temp)
#         avg = (add / length)
#         avg_rounded = round(avg,2)
#     province_temperature.append(province_temp)
#     average.append(avg_rounded)
# for i in range(len(province_list)):
#     print()
#     print(province_list[i])
#     print("Temperature of a week")
#     for temp in province_temperature[i]:
#         print(temp,end=" ")
#     print()
#     print(f"The average temp of {province_list[i]} in a week is: {average[i]}.")



