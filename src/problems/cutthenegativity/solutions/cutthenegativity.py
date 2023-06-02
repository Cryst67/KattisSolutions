n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
res = []
for i in range(n):
    for j in range(n):
        if a[i][j] != -1:
            res.append([i + 1, j + 1, a[i][j]])

print(len(res))
for i in range(len(res)):
    for j in range(3):
        print(res[i][j], end=" ")
    print()