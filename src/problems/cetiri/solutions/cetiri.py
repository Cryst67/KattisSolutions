from math import gcd
l = sorted([*map(int, input().split())])
diffs = [l[1] - l[0], l[2]- l[1]]
if len(set(diffs)) == 1:
    print(l[0] - (l[1] - l[0]))
    exit()
gcdd = gcd(*diffs)
for i in range(3):
    cur = l[i]
    nxt = cur + gcdd
    if nxt not in l:
        print(nxt)
        break
