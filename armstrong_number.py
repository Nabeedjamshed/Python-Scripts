n = input("Enter a number: ")
n1 = int(n)
l = []
for i in n:
    count = (int(i) ** int(len(n)))
    l.append(count)
if sum(l) == n1:
    print(f"{n} is an Armstromg number")
else:
    print(f"{n} is not an Armstromg number")
