from math import pi
while True:
    r, m, c = map(float, input().split())
    if r ==0 and m == 0 and c == 0:
        break
    print(pi * r**2, end=' ')
    print((r*2)**2 * (c/m))
