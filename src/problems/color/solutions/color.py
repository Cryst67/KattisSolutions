from math import ceil
s, c, k = map(int, input().split())
d = sorted(list(map(int, input().split())))
start = [1]
cur = d[0]
for i in range(1, s):
    if abs(cur - d[i]) <= k: 
        start[-1] += 1
    else:
        cur = d[i]
        start.append(1)
    cur = d[i]
machines = 0
for i in range(len(start)):
    machines += ceil(start[i]/c)
print(machines)