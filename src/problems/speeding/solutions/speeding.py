n = int(input())
pt = 0
pd = 0
maxi = float('-inf')
for i in range(n):
    t, d = map(int, input().split())
    if t == 0 and d == 0:
        continue
    maxi = max(maxi, (d - pd)/(t - pt))
    pd = d
    pt = t
print(int(maxi))