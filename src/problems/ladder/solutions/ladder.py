from math import sin, radians, ceil
a,b=map(int, input().split())
mini = float('inf')
for i in range(1, b+1):
    if a/sin(b) < mini:
        mini = a/sin(radians(b))
print(ceil(mini))