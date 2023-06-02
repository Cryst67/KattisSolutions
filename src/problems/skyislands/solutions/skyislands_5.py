def iterative_dfs(graph, start_node):
    visited = [False] * (len(graph) + 1)
    stack = [start_node]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            stack.extend(neighbor for neighbor in graph[node] if not visited[neighbor])

    return visited

def is_connected(graph):
    visited = iterative_dfs(graph, 1)
    return all(visited[1:])

n, m = map(int, input().split())
g = {i + 1: set() for i in range(n)}

for _ in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)

print('YES' if is_connected(g) else 'NO')
