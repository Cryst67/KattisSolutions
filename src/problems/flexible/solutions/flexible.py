w, p = map(int, input().split())
ws = [0 for i in range(w + 1)]
ws[w] = 1
partitions = list(map(int, input().split()))
for i in range(len(partitions)):
    cur = partitions[i]
    ws[cur] = 1
    ws[w - cur] = 1
    for j in range(i - 1, -1, -1):
        cur2 = partitions[j]
        ws[cur - cur2] = 1
for i in range(1, len(ws)):
    if ws[i] == 1: print(i, end = ' ')