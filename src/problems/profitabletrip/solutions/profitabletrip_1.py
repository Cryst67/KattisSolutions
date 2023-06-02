
class Edge:
    def __init__(self, frm, to, cost) -> None:
        self.frm = frm
        self.to = to
        self.cost = cost
v, e, w = map(int, input().split())
edges = []
d= {i : False for i in range(v + 1)}
dist = [float('inf') for i in range(v + 1)]
dist[1] = 0
to_v = []
for i in range(e):
    frm, to, weight = map(int, input().split())
    if to == v: to_v.append(Edge(frm, to, -1 * weight))
    edges.append(Edge(frm, to, -1 * weight))
for i in range(v - 1):
    for edge in edges:
        if(dist[edge.frm] + edge.cost < dist[edge.to]):
            dist[edge.to] = dist[edge.frm] + edge.cost
            if dist[edge.to] < -1 * w: 
                dist[edge.to] = -1 * w
                d[edge.to] = True
for i in range(v - 1):
    for edge in edges:
        if dist[edge.frm] + edge.cost < dist[edge.to] and not d[edge.to] :
            dist[edge.to] = float('-inf')
if dist[v] != float('-inf'):
    print(min(w, -1 *  dist[v]))
else:
    dist[v] = - 1 * w
    mini = float('inf')
    for edge in to_v:
        if dist[edge.frm] == float('-inf'):
            if edge.cost < mini: mini = edge.cost
    print(min(w, -1 * dist[v] - mini))