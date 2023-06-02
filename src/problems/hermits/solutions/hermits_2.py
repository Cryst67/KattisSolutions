n = int(input())
peeps = list(map(int, input().split()))
g = {i + 1:n for i,n in enumerate(peeps)}
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    g[a] += peeps[b - 1]
    g[b] += peeps[a - 1]
mini = float('inf')
min_index = -1
for key in g:
    if g[key] < mini:
        mini = g[key]
        min_index = key
print(min_index)