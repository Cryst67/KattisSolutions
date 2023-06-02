from math import gcd
n = int(input())
l = list(map(int, input().split()))
r = l[0]
for i in range(1, n):
    d = gcd(r, l[i])
    print(f"{r//d}/{l[i]//d}")
