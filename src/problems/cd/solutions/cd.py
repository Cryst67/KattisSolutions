import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == m == 0: break
    d = {}
    d2 = {}
    for i in range(n):
        d[int(input())] = 1
    for j in range(m):
        d2[int(input())] = 1
    count = 0
    for key in d:
        if key in d2:
            count += 1
    print(count)
    