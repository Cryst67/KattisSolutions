from math import dist
x, y, x1, y1, x2, y2 = map(int, input().split())
d = float('inf')
for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        distance = dist([x, y], [i, j])
        if distance < d:
            d = distance
print(d)