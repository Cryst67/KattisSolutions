n, m = map(int, input().split())
l = [i + 1 for i in range(n)]
for i in range(m):
    a = int(input())
    b = a + 1
    temp = l[a - 1]
    l[a - 1] = l[b - 1]
    l[b - 1] = temp
for i in range(n):
    print(l[i])