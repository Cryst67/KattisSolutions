n, k, m = map(int, input().split())
graph = {i + 1: [] for i in range(n)}
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0 for i in range(n+1)]
s = [(k, 0)]
while s:
    node, parent = s.pop(-1)
    visited[node] = 1
    for nbr in graph[node]: 
        if not visited[nbr]:
            s.append((nbr, node))
        elif nbr != parent:
            if nbr == k:
                print('NO')
                exit()
print('YES')