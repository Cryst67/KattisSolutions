import heapq
from pprint import pprint
n = int(input())
w_in = list(map(int, input().split()))
queue = []
for i in range(len(w_in)):
    for j in range(len(w_in)):
        if i == j: continue
        heapq.heappush(queue, (w_in[i] + w_in[j], [i,j]))
cost = 0
visited = [0 for i in range(n)]
while queue:
    cur = heapq.heappop(queue)
    weight = cur[0]
    fromm, to = cur[1]
    if visited[fromm] and visited[to]:
        continue
    cost += weight
    visited[fromm] = 1
    visited[to] = 1
print(cost)