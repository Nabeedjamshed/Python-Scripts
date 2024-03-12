# print('Best 5 students names!!')
# s = set()
# for i in range(5):
#     students_names = input(f"Name of {i + 1} best student: ")
#     s.add(students_names)
# print('The set of best 5 students is: ', s)
#
#
# s = {'Nabeed', 'Talha', 'Karim', 'Awwab', 'Abyaz'}
# print('The Students who join the NED: ', s)
# print("Names of students who leave NED!!")
# for i in range(2):
#     student_names = input(f"Name of student {i+1}: ")
#     s.discard(student_names)
#     s.discard(student_names)
#
# print('Remaining students are: ', s)
#
# best_dishes = {'Biryani', 'Zinger', 'Pizza', 'Roll', 'Icecream'}
# print(best_dishes)
# for i in range(len(best_dishes)):
#     best_dishes.pop()
#     print(best_dishes)
#
# items = {'Ice-cream', 'Noodles', 'Biryani', 'Cold drink', 'Beef Burger'}
# d = {}
# x = []
#
# for i in range(len(items)):
#     a = items.pop()
#     p_dishes = int(input(f"Enter the price of {a}: "))
#     x.append(p_dishes)
#     d[a] = p_dishes
#     print(p_dishes)
#
# print(d)
#
# print('YOUR BILL!!')
# print('___________________________________')
# print('ITEMS', '\t\t\t', 'PRICE')
# print('___________________________________')
#
# for j in d:
#     print(j, '\t\t\t', d[j],'\n')
#
# print(f'Total Amount = Rs. {sum(x)}', '\n')
# print(f'Maximum Price = Rs. {max(x)}', '\n')
# print(f'Minimum Price = Rs. {min(x)}', '\n')
# print('____________________________________', '\n')
# print('THANK YOU SO MUCH')
#
# universal_set = set(range(1, 41))
# s_b = set(range(1, 11))
# s_h = set(range(1, 22))
# s_c = len(universal_set) + len(s_b) - len(s_h)
# print(f'Total Students: {len(universal_set)}')
# print(f'Students who play only hockey: {len(s_h)}')
# print(f'Students who play only cricket: {s_c}')
# print(f'Students who play both: {len(s_b)}')

dog = set(range(1, 84))
cat = set(range(47, 148))
fish = set(range(72, 78)) | set(range(138, 154)) | set(range(1, 9))
other = set(range(155, 189))

only_dog = dog - (cat | fish)
only_cat = cat - (dog | fish)
only_fish = fish - (dog | cat)
total = dog | fish | cat | other
only_cat_and_dog = (cat & dog) - fish
only_cat_and_fish = (cat & fish) - dog
only_dog_and_fish = (dog & fish) - cat
all_three = cat & fish & dog

print('\n',"Data that given!!",'\n')
data = {
    "dog product": len(dog),
    "cat product": len(cat),
    "fish product": len(fish),
    "a cat and a dog product": len(only_cat_and_dog),
    "a dog and a fish product": len(only_dog_and_fish),
    "a cat and a fish product": len(only_cat_and_fish),
    "a cat, a fish and a dog product": len(all_three),
    "a product other than a cat, dog and a fish product": len(other)
}

for i, j in data.items():
    print(f"People who purchased {i} = {j}")

print('\n',"Answers",'\n')
print("People who purchased only dog product:", len(only_dog))
print("People who purchased only cat product:", len(only_cat))
print("People who purchased a dog or a fish product:", len(only_fish | only_dog))
print("Total purchases =", len(total))
