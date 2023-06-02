from math import gcd
def lcm(a, b):
    return (a * b) // gcd(a, b)
f = float('inf')
c1_c2 = []
for i in range(int(input())):
    y, c1, c2 = map(int, input().split())
    f = min(f, (y + lcm(c1, c2)))
print(f)