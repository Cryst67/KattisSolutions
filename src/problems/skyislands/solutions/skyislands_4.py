n, m = map(int, input().split())
g = {i + 1 : set() for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    if a == b: continue
    g[a].add(b)
    g[b].add(a)

visited = [0 for i in range(n + 1)]
s = [1]
while s:
    v = s.pop()
    if not visited[v]: 
        visited[v] = 1
        for nbr in g[v]:
            if not visited[nbr]:
                s.append(nbr)
                
print('YES' if all(visited[1:]) else 'NO')