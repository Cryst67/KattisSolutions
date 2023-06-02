from math import sqrt
for _ in range(int(input())):
    x, y = map(int, input().split())
    h = (y + x - sqrt((y+x) * (y+x) - 3 * x * y)) / 6
    print((x - 2 * h) * (y - 2 * h) * h)