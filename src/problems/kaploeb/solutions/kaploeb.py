l, k, s = map(int, input().split())
d = {}
for _ in range(l):
    line = input().split()
    n = int(line[0])
    time = line[1].split('.')
    score = int(time[0]) * 60 + int(time[1])
    if n in d:
        d[n][0] += score
        d[n][1] += 1
    else:
        d[n] = [score, 1]

final = d.copy()
for key in d:
    if d[key][1] < k: final.pop(key)

final = sorted(final, key=lambda x: (final[x][0], x))
for num in final:
    print(num)
