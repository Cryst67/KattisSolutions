from math import ceil
c, n, m = map(int, input().split())
d = {}
for i in range(n):
    ci = int(input())
    if ci in d: d[ci] += 1
    else: d[ci] = 1
days = [0 for i in range(51)]
for i in range(51): 
    new_d = {}
    count = 0
    for key in d:
        count += d[key]
        k, v = key, d[key]
        k*=2
        if k <= c: 
            if k in new_d:
                new_d[k] += v
            else: new_d[k] = v
        else:
            k1 = ceil(k/2)
            k2 = k//2
            if k1 in new_d:
                new_d[k1] += v
            else: new_d[k1] = v
            if k2 in new_d:
                new_d[k2] += v
            else: new_d[k2] = v
    days[i] = count
    d = new_d
for i in range(m):
    print(days[int(input())])