n = int(input())
l = sorted(list(map(int, input().split())))
f = [l[0]]
for i in range(1, n):
    if abs(l[i] - l[i - 1]) > 1:
        f.append(l[i])
    
print(sum(f))