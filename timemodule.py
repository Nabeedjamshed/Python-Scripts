import time
# t = time.localtime() # No need of this line
# t1 = time.strftime("%Y-%m-%d %H:%M:%S")
# print(t1)

# print(4)
# t = time.sleep(10) # agr ksi line ya method ko wait krana ke ye itne time ke baad run ho tu time.sleep() method use krskte.
# print("Hello Nabeed")

# def usingwhile():
#     i = 0
#     while i<5000:
#         i += 1
#         print(i)
# def usingfor():
#     for i in range(5000):
#         print(i)
# come = time.time()
# usingwhile()
# whiletimeuse = time.time() - come
# come = time.time()
# usingfor()
# print("While",whiletimeuse)
# print("For",time.time() - come)




# Get the current timestamp
timestamp = time.time()

# Convert the timestamp to local time
local_time = time.localtime(timestamp)

# Print the local time tuple
print(local_time)

