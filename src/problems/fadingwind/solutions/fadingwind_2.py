h, k, v, s = map(int, input().split())
c = 0
while h > 0:
    v += s
    v -= max(1, int(v/10))
    if v >= k:
        h += 1
    if v > 0 and v < k:
        h-= 1
    if h == 0:
        v = 0
    if v <= 0:
        h = 0
        v = 0
    if s > 0:
        s -= 1
    c += v
print(c)