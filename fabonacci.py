# def fabonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fabonacci(n-2) + fabonacci(n-1)
# num = int(input("Enter the number: "))
# for i in range(num+1):
#     print(fabonacci(i),end=' ')


# class Solution:
#     def __init__(self):
#         self.memo = {}
    
#     def fabonacci(self,n:int):
#         if n in self.memo:
#             return self.memo[n]
#         if n==0:
#             return 0
#         elif n==1:
#             return 1
#         else:
#             result =  self.fabonacci(n-2) + self.fabonacci(n-1)
#             self.memo[n] = result
#             return result
# num = int(input())
# s = Solution()
# s.fabonacci(num)