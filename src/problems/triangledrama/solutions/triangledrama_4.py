from pprint import pprint
n = int(input())
g = []
f = [[] for i in range(n)]
scores = {}
for i in range(n):
    l = list(map(int, input().split()))
    f[i] = l
maxi = 0
maxindes = []
for i in range(n):
    for j in range(i + 1, n):
            for k in range(j+1, n):
                g.append([i+1, j + 1])
                g[-1].append(k + 1)
                x, y, z = g[-1]
                score = 1
                score *= f[x - 1][y - 1]
                score *= f[x - 1][z - 1]
                score *= f[y - 1][z - 1]
                if score > maxi:
                     maxi = score
                     maxindes = [x, y, z]
for i in range(3):
    print(maxindes[i], end = ' ')
print()
     