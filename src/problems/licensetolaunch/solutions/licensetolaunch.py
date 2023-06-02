n = int(input())
l = list(map(int, input().split()))
mini = float('inf')
minind = -1
for i in range(n):
    if l[i] < mini:
        mini = l[i]
        minind = i
print(minind)