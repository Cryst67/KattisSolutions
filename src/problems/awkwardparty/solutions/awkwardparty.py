prev = {}
n = int(input())
l = list(map(int, input().split()))
mini = float('inf')
for i in range(n):
    num = l[i]
    if num not in prev:
        prev[num] = i
        continue
    mini = min(mini, i - prev[num])
    prev[num] = i
print(n if mini == float('inf') else mini)