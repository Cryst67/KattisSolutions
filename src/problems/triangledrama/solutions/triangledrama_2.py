n = int(input())
f = []

for i in range(n):
    l = list(map(int, input().split()))
    f += [l]

maxi = 0
maxindes = []

def get_score_info(f, indices):
    x, y, z = indices
    return (f[x - 1][y - 1] * f[x - 1][z - 1] * f[y - 1][z - 1])

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j+1, n):
            indes = i + 1, j + 1, k + 1
            score = get_score_info(f, indes)
            if score > maxi:
                 maxi = score
                 maxindes = indes

x, y, z = maxindes
print(x, y, z)