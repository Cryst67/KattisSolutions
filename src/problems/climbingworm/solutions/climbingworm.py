a, b, h = map(int, input().split())
s = 0
c = 0
while s < h:
    c += 1
    s += a
    if s >= h: break
    else: s -= b
print(c)