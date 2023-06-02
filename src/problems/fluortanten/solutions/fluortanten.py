n = int(input())
hap = list(map(int, input().split()))
hap.remove(0)
hap.insert(0, 0)
s = sum([(i + 1) * hap[i] for i in range(n)])
ans = s
for i in range(n - 1):
    s -= hap[i + 1]
    ans = max(ans, s)
print(ans)