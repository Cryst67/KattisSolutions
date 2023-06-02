from math import ceil
a, b, c = map(int, input().split())
a -= 1
g = b//c
day = a/g
if a % g > 0:
    day += 1
print(int(day))