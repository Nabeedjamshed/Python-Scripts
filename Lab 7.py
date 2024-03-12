# def province():
#     names = ()
#     tup = list(names)
#     province_name = input("Enter the name of a province: ")
#     while province_name or province_name != '':
#         tup.append(province_name)
#         names = tuple(tup)
#         province_name = input("Enter the name of a province: ")
#     print(names)
# province()

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
if len(word1) == len(word2) + 1:
    print(f"The word {word1} has 1 more character than the word {word2}.")
else:
    print(f"The word {word1} has no 1 more character than the word {word2}.")

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
if word1 < word2:
    print(f"The word {word1} appears earlier in the dictionary than the word {word2}.")
else:
    print(f"The word {word1} does not appears earlier in the dictionary than the word {word2}.")

word = input("Enter a word: ")
if 'e' not in word:
    print(f"The letter e does not appear in the word {word}.")
else:
    print(f"The letter e appear in the word {word}.")

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word3 = input("Enter the second word: ")
if len(word1) == len(word2) + len(word3):
    print(f"The number of characters in word {word1} is equal to "
          f"the sum of the numbers of characters in words {word2} and {word3}")
else:
    print(f"The number of characters in word {word1} is not equal to "
          f"the sum of the numbers of characters in words {word2} and {word3}")

# import math

# x = []
# y = []
# for i in range(4):
#     print("For Hit # ", i+1)
#     x.append(int(input("Enter x-coordinate: ")))
#     y.append(int(input("Enter y-coordinate: ")))
#     if math.sqrt((x[i]) ** 2 + (y[i]) ** 2) <= 10:
#         print("You Hit it.\n")
#     else:
#         print("You Missed.\n")
#
# sample = [(2, 3), (4, 7), (8, 11), (3, 6)]
# x = []
# y = []
# for i in sample:
#     x.append(min(i))
#     y.append(max(i))
# for j in range(len(x)):
#     print("Tuple #", j+1)
#     print("MINIMUM = ", x[j], "\nMAXIMUM = ", y[j])
#     print()