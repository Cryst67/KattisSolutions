n = int(input())
l = []
for i in range(n):
    a, b = input().split()
    b = float(b)
    l.append(b)
l.sort(reverse=1)
f = 0
for i in range(n):
    f += (i + 1) * l[i]
print(f)