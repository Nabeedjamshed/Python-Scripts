def my_generator():
    for i in range(6):
        yield i
gen = my_generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

#OR

for j in gen:
    print(j)