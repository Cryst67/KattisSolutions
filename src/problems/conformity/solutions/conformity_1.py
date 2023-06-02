n = int(input())
u = 0
d = {}
a = []
for i in range(n):
    s = list(map(int, input().split()))
    s.sort()
    s = list(map(str, s))
    s = ''.join(s)
    if s in d:
        d[s] +=1
    else:
        d[s] = 1
maxi = float('-inf')
all_equal = True
prev = 0
for key in d:
    prev = d[key]
    break
for key in d:
    if d[key] > maxi:
        maxi = d[key]
    if prev != d[key]:
        all_equal = False

total = 0
for key in d:
    if d[key] == maxi:
        total += d[key]
print(total)