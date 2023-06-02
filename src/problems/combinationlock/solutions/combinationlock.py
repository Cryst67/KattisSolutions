while True:
    p, c1, c2, c3 = map(int, input().split())
    if p == c1 == c2 == c3 == 0: break
    deg = 720
    if p < c1: deg += 9*(40 - c1 + p)
    elif c1 < p: deg += 9 * abs(c1 - p)
    deg += 360
    if c1 > c2: deg += ((40 - c1) + c2)*9
    elif c2 > c1: deg += abs(c1 - c2)*9
    if c2 > c3: deg += abs(c2 - c3)*9
    elif c3 > c2: deg += 9*(40- c3 + c2)
    print(deg)