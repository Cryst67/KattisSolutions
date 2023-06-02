from collections import deque
v, e = map(int, input().split())
graph = {i + 1: [] for i in range(v)}
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
def topological_sort(graph):
    in_degrees = {vertex: 0 for vertex in graph}
    for _, neighbors in graph.items():
        for neighbor in neighbors:
            in_degrees[neighbor] += 1
    queue = deque([vertex for vertex, in_degree in in_degrees.items() if in_degree == 0])
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)
    return result

ordering = [0, *topological_sort(graph)]
dist = {}
for i in ordering: dist[i] = [1, i]
max_vertex = 1
for i in range(1, len(ordering)):
    vertex = ordering[i]
    for nbr in graph[vertex]:
        if dist[nbr][0] < dist[vertex][0] + 1:
            dist[nbr] = [dist[vertex][0] + 1, vertex]
        if dist[nbr][0] >= dist[max_vertex][0]:
            max_vertex = nbr
d = dist[max_vertex][0]
print(d)
order = [0 for i in range(d)]
order[d - 1] = max_vertex
d-=1
while max_vertex != dist[max_vertex][1]:
    d -= 1
    max_vertex = dist[max_vertex][1]
    order[d] = max_vertex
print(' '.join(map(str, order)))