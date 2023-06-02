from pprint import pprint
r, c, zr, zc = map(int, input().split())
g = [0 for _ in range(r)]
for i in range(r):
    g[i] = list(input())
f = [] 
for i in range(r):
    new_c = []
    for j in range(c):
        for k in range(zc):
            new_c.append(g[i][j])
    for j in range(zr):
        f.append(new_c)
        
for i in range(len(f)):
    for j in range(len(f[i])):
        print(f[i][j], end='')
    print()