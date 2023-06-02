n = int(input())
l = [0, *map(int, input().split())]
for i in range(1, n + 1):
    indices = [i * j for j in range(1, n//i + 1)]
    if len(indices) < 2: continue
    flag = 1
    for j in range(len(indices) - 1):
        if l[indices[j]] < l[indices[j + 1]]:
            continue
        else: flag = 0
    if flag: 
        print(i)
        exit()
print('ABORT!')