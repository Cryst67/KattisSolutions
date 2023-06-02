from functools import reduce
alphabet='abcdefghijklmnopqrstuvwxyz'
n, t = map(int, input().split())
a = list(map(int, input().split()))

if t == 1:
    print(7)
elif t == 2:
    if a[0] > a[1]: print('Bigger')
    elif a[0] == a[1]: print('Equal')
    else: print('Smaller')
elif t == 3:
    l = sorted(a[:3])
    print(l[1])
elif t == 4:
    print(sum(a))
elif t == 5:
    print(reduce(lambda x, y: x + y, list(filter(lambda x: x% 2 == 0, a))))
elif t == 6:
    print(''.join(list(map(lambda x: alphabet[x], list(map(lambda x: x % 26, a))))))
elif t == 7:
    i = 0
    visited = [0 for i in range(n)]
    while True:
        if i < 0 or i > n - 1:
            print('Out')
            break
        elif i == n - 1:
            print('Done')
            break
        if visited[i]:
            print('Cyclic')
            break
        visited[i] = 1
        i = a[i]
