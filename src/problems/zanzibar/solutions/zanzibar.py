n = int(input())
for i in range(n):
    pops = list(map(int, input().split()))
    imports = 0
    for j in range(1, len(pops)):
        if pops[j - 1] * 2 < pops[j]:
            imports += pops[j] - 2 * pops[j - 1]
    print(imports)