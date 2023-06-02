n, t = map(int, input().split())
l = sorted(list(map(int, input().split())))

if t == 1:
    d = {}
    found = 0
    for num in l:
        if num in d:
            print('Yes')
            found = 1
            break
        d[7777 - num] = 1
    if not found:
        print('No')
elif t == 2:
    if len(set(l)) == len(l):
        print('Unique')
    else: print('Contains duplicate')
elif t == 3:
    d = {}
    for num in l:
        if num in d:
            d[num] += 1
        else: d[num] = 1
    found = 0
    for key in d:
        if d[key] > n//2:
            print(key)
            found = 1
            break
    if not found: print(-1)
elif t == 4:
    if len(l) % 2 != 0:
        print(l[n//2])
    else: print(l[n//2  - 1], l[n//2])
elif t == 5:
    for num in l:
        if num > 99 and num < 1000:
            print(num, end=' ')
    print()
