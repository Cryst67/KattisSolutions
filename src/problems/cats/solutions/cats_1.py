import heapq
t = int(input())
for _ in range(t):
    m, c = map(int, input().split())
    if m < c: 
        print('no')
        continue
    pq = []
    graph = {i:[] for i in range(c)}
    visited = [False for i in range(c)]
    for i in range(int(c*(c-1)/2)):
        fromm, to, weight = map(int, input().split())
        graph[fromm].append((weight, to))
        graph[to].append((weight, fromm))
    mstEdges = c - 1
    edgeCount, mstCost = 0, 0
    nodeIndex = 0
    visited[nodeIndex] = True
    edges = graph[nodeIndex]
    for edge in edges:
        if not visited[edge[1]]:
            heapq.heappush(pq, edge)
    while len(pq) != 0 and edgeCount != mstEdges:
        edge = heapq.heappop(pq)
        nodeIndex = edge[1]
        if visited[nodeIndex]: continue
        edgeCount += 1
        mstCost += edge[0]
        visited[nodeIndex] = True
        edges = graph[nodeIndex]
        for edge in edges:
            if not visited[edge[1]]:
                heapq.heappush(pq, edge)
    totalCost = mstCost + c
    if totalCost <= m: print('yes')
    else: print('no')