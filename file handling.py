# with open('kind.txt', 'w') as f:
#     content = f.write('There are several kinds of animals exits in the world')
#     print(content)
# with open('kind.txt', 'rb') as f:
#     content = f.read()
#     print(content)

# with open('hello.txt', 'r') as f:
#     content = f.read()
#     print(content)
#     print(type(content))
# f = open('myfile.txt', 'w')
#
# f = open('myfile.txt', 'r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1}")
#   print(f"Marks of student {i} in English is: {m2}")
#   print(f"Marks of student {i} in SST is: {m3}")
#
#   print(line)

# f = open('myfile.txt', 'r')
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     # lst = ['Math', 'English', 'SST']
#     # for j in lst:
#     m1 = int(line.split(',')[0])
#     m2 = int(line.split(',')[1])
#     m3 = int(line.split(',')[2])
#     print(f'Marks of student {i} in Math is {m1} ')
#     print(f'Marks of student {i} in SST is {m2} ')
#     print(f'Marks of student {i} in English is {m3} ')
#     print(line)

f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.writelines(line + '\n')


# f = open('myfile.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()


# with open('file.txt', 'r') as f:
#     print(type(f))
#     # Move to the 10th byte in the file
#     f.seek(10)
#     print(f.tell())
#     # Read the next 5 bytes
#     data = f.read(6)
#     print(data)

# with open('file.txt', 'r') as f:
#   # Read the first 10 bytes
#   data = f.read(10)
#
#   # Save the current position
#   current_position = f.tell()
#
#   # Seek to the saved position
#   f.seek(current_position)

# with open('sample.txt', 'w') as f:
#     f.write('Hello World!')
#     f.truncate(5)
# with open('sample.txt', 'r') as f:
#     content = f.read()
#     print(content)