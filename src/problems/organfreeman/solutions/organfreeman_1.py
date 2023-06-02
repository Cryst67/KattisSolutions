memo = [0 for i in range(10)]

def factorial(n):
    if n == 1: return 1
    if memo[n] != 0: return memo[n]
    memo[n] = n*factorial(n-1)
    return memo[n]

num = int(input())
n = 9
s = ''
if num == 1:print(0);exit()
while num != 0:
    if factorial(n) <=  num:
        num -= factorial(n)
        s += str(n)
    else: n -= 1
print(s[::-1])