from heapq import heappop, heappush
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    d = 0
    for i in range(1, n):
        d+= (l[i] - l[i - 1])
    d += (l[-1] - l[0])
    print(d)