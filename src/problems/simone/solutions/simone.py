n, k = map(int, input().split())
l = list(map(int, input().split()))
dat = [0 for i in range(k + 1)]
for i in range(n):
    dat[l[i]] += 1
mini = min(dat[1:])
final = []
for i in range(1, k + 1):
    if dat[i] == mini:
        final.append(i)
print(len(final))
print(' '.join(map(str, final)))