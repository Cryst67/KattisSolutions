#basic bfs
n = int(input())

for _ in range(n):
    n, m = map(int, input().split())
    graph = {i + 1: [] for i in range(n)}
    visited = [0 for i in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    queue = [1]
    visited[1] = 1
    pilots = 0
    while queue:
        city = queue.pop(0)
        for nbr in graph[city]:
            if not visited[nbr]:
                queue.append(nbr)
                visited[nbr] = 1
                pilots += 1
    print(pilots)