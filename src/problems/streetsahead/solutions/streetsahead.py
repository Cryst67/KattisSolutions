n, q = map(int, input().split())
d = {}
for i in range(n):
    d[input()] = i
c = []
for i in range(q):
    c.append(input())

for pair in c:
    a, b = pair.split()
    print(abs(d[a] - d[b]) - 1)