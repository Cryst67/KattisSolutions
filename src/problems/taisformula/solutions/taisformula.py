n = int(input())
area = 0
pt = 0
pv = 0
for i in range(n):
    t, v = map(float, input().split())
    if pt == 0 and pv == 0:
        pv = v
        pt = t
        continue
    area += (v + pv)/2 * (t - pt)
    pv = v
    pt = t

print(area/1000)