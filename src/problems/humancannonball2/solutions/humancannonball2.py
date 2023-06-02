from math import sin, cos, radians
GRAVITY = 9.81 
res = []
n = int(input())
for _ in range(n):
    v, theta, x1, h1, h2 = map(float, input().split())
    t = x1/(v*cos(radians(theta)))
    y = (v * t * sin(radians(theta))) - .5*GRAVITY*(t**2)
    if y - h1 >= 1 and h2 - y >= 1:
        res.append('Safe')
    else: res.append('Not Safe')

for r in res: print(r)