def update_even(c, n):
    if n % 2 == 0: return c + 1
    return c
n, m = map(int, input().split())
l = [*map(int, input().split())]
c,e = 0,0
for i in range(n - (m - 1)):
    if i == 0:
        for j in range(m):
            e = update_even(e, l[j])
        if e > 1: c += 1
        continue
    if l[i - 1] % 2 == 0: e -= 1
    e = update_even(e, l[i + (m - 1)])
    if e > 1: c += 1
print(c)
