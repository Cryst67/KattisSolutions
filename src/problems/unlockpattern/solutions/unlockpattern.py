from math import dist
grid = [[] for i in range(3)]
for i in range(3):
    grid[i] = list(map(int, input().split()))
start = 1
start_indices = []
length = 0
for i in range(3):
    for j in range(3):
        if grid[i][j] == 1:
            start_indices = (i, j)
            break
    else:
        continue
    break
while start != 9:
    for i in range(3):
        for j in range(3):
            if grid[i][j] == start + 1:
                length += dist(start_indices, (i, j))
                start_indices = (i, j)
                start += 1
                break
        else:
            continue
        break
print(length)