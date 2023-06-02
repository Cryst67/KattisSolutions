from math import factorial
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