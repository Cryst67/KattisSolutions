n, k = map(int, input().split())
l = [i for i in range(2, n + 1)]
visited = [0 for i in range(n + 1)]
crosses = 0
prev = -1
for i in range(2, n + 1):
    for j in range(1, n//i + 1):
        if visited[i * j]: continue
        visited[i * j] = 1
        crosses += 1
        prev = i * j
        if crosses == k:
            print(prev)
