l = []
n = int(input())
for i in range(n):
    l.append(int(input()))
l = sorted(l, reverse=1)
l.insert(0, 0)
s = 0
for i in range(1, n+1):
    if i % 3 ==0: continue
    s += l[i]
print(s)