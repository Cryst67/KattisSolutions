r, c = map(int, input().split())
grid = []
for _ in range(r):
    grid.append(input())
count = 0
for i in range(c):
    blanks = 1
    for j in range(r):
        if grid[j][i] != '_':
            blanks = 0; break
    if blanks: count += 1
print(count + 1)