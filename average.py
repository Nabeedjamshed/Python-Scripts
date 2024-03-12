def replace_with_avg(lst):
    avg = (lst[0]+lst[len(lst)//2]+lst[-1])/3
    lst[0], lst[len(lst) // 2], lst[-1] = avg, avg, avg
    return lst
list = [10, 7, 4, 9, 5, 18, 2, 1, 8, 11, 12, 6, 3, 1, 11, 24]
print(replace_with_avg(list))

