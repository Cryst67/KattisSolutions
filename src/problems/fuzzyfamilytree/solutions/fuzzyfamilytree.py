import sys

class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.num_sets = N

    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def union(self, i, j):
        if not self.is_same_set(i, j):
            self.num_sets -= 1
            x, y = self.find_set(i), self.find_set(j)
            if self.rank[x] > self.rank[y]: self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]: self.rank[y] += 1

v, g = int(input()), {}
ufds = UFDS(v)
wait = []
for line in sys.stdin:
    a, r, b = line.split()
    a, b = ufds.find_set(int(a)), ufds.find_set(int(b))
    if r == '?': ufds.union(a, b)
    else: wait.append((a, b))

added = set()
indeg = {}
for a, b in wait:
    a, b = ufds.find_set(int(a)), ufds.find_set(int(b))
    if a not in g: g[a] = set()
    g[a].add(b)
    if a not in indeg: indeg[a] = 0
    if b not in indeg: indeg[b] = 0
    indeg[b] += 1

if g:
    for i in indeg:
        if indeg[i] == 0:
            enar = i
            break
    print(*list(filter(lambda x: ufds.find_set(x) == enar, range(v))))
else: print(*range(v))