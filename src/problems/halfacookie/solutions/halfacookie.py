from math import sin, asin, degrees, radians, dist, pi
while True:
    try: r, x, y = map(float, input().split())
    except EOFError: break
    d = dist([0, 0], [x, y])
    if r - d < 0.001: 
        print('miss')
        continue
    angle = radians(2 * (90 - degrees(asin(d/r))))
    area = .5 * (angle - sin(angle)) * (r ** 2)
    print(pi * (r ** 2) - area, area)

