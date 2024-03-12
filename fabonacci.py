def fabonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabonacci(n-2) + fabonacci(n-1)
num = int(input("Enter the number: "))
for i in range(num+1):
    print(fabonacci(i),end=' ')