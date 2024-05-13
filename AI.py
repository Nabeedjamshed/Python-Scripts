l = []
n1 = input().split()
for i in n1:
    if i == ',':
        continue
    else:
        n2 = i
        n3 = int(n2)
        l.append(n3)
print(l)
