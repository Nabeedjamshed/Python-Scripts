# def stats(filename):
#     with open(filename, "r") as f:
#         text = f.read()

#     lines = text.splitlines()
#     line_count = len(lines)

#     words = text.split()
#     word_count = len(words)

#     char_count = len(text)

#     print(f"line count: {line_count}")
#     print(f"word count: {word_count}")
#     print(f"character count: {char_count}")
#     print()
# stats('example.txt')

# def distribute(file):
#     with open(file, 'r') as g:
#         content = g.read().split()

#     a_positive = content.count('A+')
#     a_negative = content.count('A-')
#     b_positive = content.count('B+')
#     b_negative = content.count('B-')
#     c_positive = content.count('C+')
#     c_negative = content.count('C-')
#     d = content.count('D')
#     f = content.count('F')

#     print("Total strength of class", len(content))
#     print(a_positive, 'got A+')
#     print(a_negative, 'got A-')
#     print(b_positive, 'got B+')
#     print(b_negative, 'got B-')
#     print(c_positive, 'got C+')
#     print(c_negative, 'got C-')
#     print(d, 'got D')
#     print(f, 'got F')

# distribute('grades.txt')


# def has_duplicates(filename):
#     with open(filename, 'r') as f:
#         lines = f.readlines()

#     seen_lines = set()

#     for line in lines:
#         if line in seen_lines:
#             return True
#         else:
#             seen_lines.add(line)

#     return False

# result1 = has_duplicates('Duplicates.txt')
# result2 = has_duplicates('noDuplicates.txt')
# print(result1)
# print(result2)


def abc(file):
    with open(file, 'w') as w:
        d = w.write(f"I will tell you my secret. But first, I have to explain "
                    f"why it is a secret. And that is all I will tell you about my secret.")

    with open(file, 'r') as r:
        data = r.read()

    with open('crypto.txt', 'w') as f:
        f.write(data)

    file = open('crypto.txt', 'r')
    d1 = file.read()
    word = d1.split()
    for i in word:
        if len(i) == 4:
            print('XXXX', end=' ')
        else:
            print(i, end=' ')


abc('example.txt')




