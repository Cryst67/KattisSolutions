n = int(input())
l = list(map(int, input().split()))
uniques = [l[0]]
for i in range(1, n):
    if l[i] != l[i - 1]: uniques += [l[i]]
maxi = 0
l = uniques
n = len(l)
for i in range(n):
    if i == 0 or i == n - 1: continue
    li, ri = i - 1, i + 1
    left, rite, mid = l[li], l[ri], l[i]
    if left > mid or rite > mid: continue
    while True:
        li -= 1
        if li == -1: break
        if l[li] > left: break
        left = l[li]
    while True:
        ri += 1
        if ri == n: break
        if l[ri] > rite: break
        rite = l[ri]
    maxi = max(maxi, min(mid - left, mid - rite))
print(maxi)