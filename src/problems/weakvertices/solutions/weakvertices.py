from pprint import pprint
while True:
    n = int(input())
    if n == -1:
        break
    d = { i:[] for i in range(n) }
    for i in range(n):
        d_at_i = list(map(int, input().split()))
        for j in range(len(d_at_i)):
            if d_at_i[j] == 1:
                d[i].append(j)
    non_t = []
    t = [0 for i in range(n)]
    for key in d:
        if t[key] == 1:
            continue
        if len(d[key]) < 2:
            non_t.append(key)
        for neighbor in d[key]:
            for another_neighbor in d[neighbor]:
                if another_neighbor in d[key]:
                    t[key] = 1
                    t[neighbor] = 1
    for i in range(len(t)):
        if t[i] == 0:
            print(i, end=' ')
    print()