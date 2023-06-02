import time
class UnionFind:
    def __init__(self, n) -> None:
        self.id = [i for i in range(n)]
        self.sz = [1 for _ in range(n)]
    def find(self, p):
        root = p
        while root != self.id[root]: root = self.id[root]
        while p != root: #path compression
            nxt = self.id[p]
            self.id[p] = root
            p = nxt
        return root
    def connected(self, p, q): return self.find(p) == self.find(q)
    def size(self, p): return self.sz[self.find(p)]
    def union(self, p, q):
        r1 = self.find(p)
        r2 = self.find(q)
        if r1 == r2: return
        if self.sz[r1] < self.sz[r2]:
            self.sz[r2] += self.sz[r1]
            self.id[r1] = r2
        else: 
            self.sz[r1] += self.sz[r2]
            self.id[r2] = r1

class Edge:
    def __init__(self, frm, to, cost) -> None:
        self.frm = frm
        self.to = to
        self.cost = cost

m_d = lambda x, y, x1, y1: abs(x - x1) + abs(y - y1)
n = int(input())
l = []
for i in range(n):
    x, y = map(int, input().split())
    l += [(x, y)]
edges = []
for i in range(n):
    x, y = l[i]
    for j in range(i + 1, n):
        x1, y1 = l[j]
        edges += [Edge(i, j, m_d(x, y, x1, y1))]
start_time = time.time()
edges.sort(key=lambda x: x.cost)
elapsed_time = time.time() - start_time
if elapsed_time > 3: raise RuntimeError
time = 0
uf = UnionFind(n)
for edge in edges:
    p, q = edge.frm , edge.to
    if uf.connected(p, q): continue
    uf.union(p, q)
    time += edge.cost
    if uf.size(0) == n: break
print(time * 2)