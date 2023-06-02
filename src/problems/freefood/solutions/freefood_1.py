l = [0 for i in range(366)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        l[i] = 1
print(l.count(1))