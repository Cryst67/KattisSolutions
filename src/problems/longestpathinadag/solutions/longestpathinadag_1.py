v, e  = map(int, input().split())
graph = {i + 1: [] for i in range(v)}
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

from collections import deque

def topological_sort(graph):
    # Calculate in-degrees for all vertices
    in_degrees = {vertex: 0 for vertex in graph}
    for _, neighbors in graph.items():
        for neighbor in neighbors:
            in_degrees[neighbor] += 1

    # Create a queue with all vertices that have no incoming edges
    queue = deque([vertex for vertex, in_degree in in_degrees.items() if in_degree == 0])

    # Initialize result list
    result = []

    # Process vertices in queue
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycles
    if len(result) != len(graph):
        raise ValueError("Input graph has a cycle")

    return result

ordering = [0, *topological_sort(graph)]
dist = {}
for i in ordering:
    if i == 0: continue
    dist[i] = [1, i]
max_vertex = 1
for i in range(1, len(ordering)):
    vertex = ordering[i]
    if vertex not in graph: continue
    for nbr in graph[vertex]:
        if nbr not in dist: continue
        if dist[nbr][0] < dist[vertex][0] + 1:
            dist[nbr] = [dist[vertex][0] + 1, vertex]
        if dist[nbr][0] >= dist[max_vertex][0]:
            max_vertex = nbr
f = dist[max_vertex][0]
print(f)
order = [0 for i in range(f)]
f -= 1
order[f] = max_vertex
f -= 1
while max_vertex != dist[max_vertex][1]:
    max_vertex = dist[max_vertex][1]
    order[f] = max_vertex
    f -= 1
print(' '.join(map(str, order)))