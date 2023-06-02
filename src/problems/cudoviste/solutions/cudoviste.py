r, c = map(int, input().split())
g = []
for i in range(r):
    g.append(input())
a = [0,0,0,0,0]
for i in range(r - 1):
    for j in range(c - 1):
        cars = 0
        if g[i][j] == 'X':
            cars+=1
        if g[i][j + 1] == 'X':
            cars+=1
        if g[i + 1][j] == 'X':
            cars+=1
        if g[i + 1][j + 1] == 'X':
            cars+=1
        if g[i][j] == '#':
            continue
        if g[i][j + 1] == '#':
            continue
        if g[i + 1][j] == '#':
            continue
        if g[i + 1][j + 1] == '#':
            continue
        a[cars]+=1

for n in a:
    print(n)