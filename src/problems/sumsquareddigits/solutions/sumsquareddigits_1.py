from functools import reduce
p = int(input())
for i in range(p):
    k, b, n = map(int, input().split())
    a = []
    while n != 0:
        rem = n % b
        n -= rem
        n = n/b
        a.append(rem)
    print(k, int(reduce(lambda x, y: x+ y,list(map(lambda x: x ** 2, a)),0)))