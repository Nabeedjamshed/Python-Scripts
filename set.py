# items = {'Ice-cream', 'Noodles', 'Biryani', 'Cold drink', 'Beef Burger'}
# d = {}
# x = []

# for i in range(len(items)):
#     a = items.pop()
#     p_dishes = int(input(f"Enter the price of {a}: "))
#     x.append(p_dishes)
#     d[a] = p_dishes
#     print(p_dishes)

# print(d)

# print('YOUR BILL!!')
# print('___________________________________')
# print('ITEMS', '\t\t\t', 'PRICE')
# print('___________________________________')

# for j in d:
#     print(j, '\t\t\t', d[j],'\n')

# print(f'Total Amount = Rs. {sum(x)}', '\n')
# print(f'Maximum Price = Rs. {max(x)}', '\n')
# print(f'Minimum Price = Rs. {min(x)}', '\n')
# print('____________________________________', '\n')
# print('THANK YOU SO MUCH')


# dog_product = set(range(1, 84))
# cat_product = set(range(53, 154))
# fish_product = set(range(76, 98))
# d_c = dog_product.intersection(cat_product)
# d_f = dog_product.intersection(fish_product)
# c_f = cat_product.intersection(fish_product)
# print(len(dog_product))
# print(len(cat_product))
# print(len(fish_product))
# print(len(d_c))
# print(len(d_f))
# print(len(c_f))

# Create sets for each type of product
dog = set()
cat = set()
fish = set()
other = set()

# Loop through the purchases and add them to the corresponding sets
for i in range(83):
  dog.add(i)
for i in range(101):
  cat.add(i + 83)
for i in range(22):
  fish.add(i + 184)
for i in range(34):
  other.add(i + 206)

# Calculate the intersections of the sets
dog_cat = dog.intersection(cat)
dog_fish = dog.intersection(fish)
cat_fish = cat.intersection(fish)
dog_cat_fish = dog_cat.intersection(fish)

# Subtract the intersections from the original sets to get the exclusive sets
dog_only = dog - dog_cat - dog_fish - dog_cat_fish
cat_only = cat - dog_cat - cat_fish - dog_cat_fish
fish_only = fish - dog_fish - cat_fish - dog_cat_fish

# Calculate the union of the sets
dog_or_fish = dog.union(fish)

# Calculate the total number of purchases
total = len(dog) + len(cat) + len(fish) + len(other)

# Print the answers
print("i. How many purchases were for a dog product only?")
print(len(dog_only))
print("ii. How many purchases were for cat product only?")
print(len(cat_only))
print("iii. How many purchases for a dog or a fish product?")
print(len(dog_or_fish))
print("iv. How many purchases were there in total?")
print(total)
