n = int(input())
l = sorted([*map(int, input().split())], reverse=1)
d = 0
for i in range(n):
    if (i + 1) % 3 ==0: d+= l[i]
print(d)