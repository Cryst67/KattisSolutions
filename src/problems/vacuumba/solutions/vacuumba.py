from math import sin, cos, radians
for _ in range(int(input())):
    x = y = angle = 0
    for _ in range(int(input())):
        a, h = map(float, input().split())
        angle += -a
        x += h * sin(radians(angle))
        y += h * cos(radians(angle))
    print(x, y)