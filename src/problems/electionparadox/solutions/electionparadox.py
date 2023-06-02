n = int(input())
l = sorted([*map(int, input().split())])
w=0
v=0
for i in range(n):
    if i > n//2: w=1
    if w: v+= l[i]
    else: v += l[i]//2
print(v)
