n, m = map(int, input().split())
grid = [0 for i in range(n)]
for i in range(n):
    grid[i] = list(map(int, input().split()))
mini = float('inf')
for i in range(n):
    for j in range(m):
        cost = 0
        for ii in range(n):
            for jj in range(m):
                if i == ii and j == jj: continue
                cost += grid[ii][jj]*(abs(i - ii) + abs(j - jj))
        mini = min(cost, mini)
print(mini)

