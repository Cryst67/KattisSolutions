import bisect
n, q = map(int, input().split())
l = sorted(list(map(int, input().split())))

for _ in range(q):
    t, d = map(int, input().split())
    if t == 1:
        i = bisect.bisect_right(l, d)
        if i == len(l):
            print(-1)
        else: print(l.pop(i))
    else:
        i = bisect.bisect_left(l, d)
        if i == len(l):
            print(l.pop(i - 1))
        elif l[i] <= d:
            print(l.pop(i))
        else: print(-1)