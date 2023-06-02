n = int(input())
visited = [0 for _ in range(n + 1)]
l = [0, *list(map(int, input().split()))]
swaps = 0
for i in range(1, n + 1):
    if visited[i]: continue
    if l[i] == i: 
        visited[i] = 1
        continue
    j = l[i]
    while j != i:
        visited[j] = 1
        j = l[j]
        swaps += 1
print(swaps)
