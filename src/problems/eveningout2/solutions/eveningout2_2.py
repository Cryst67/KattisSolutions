a, b = map(int, input().split())
mini = float('inf')
ans = -1
for i in range(1, int(a**.5)+1):
    if a % i == 0:
        mini = min(mini, abs(i - b), abs(a//i - b))
print(mini)