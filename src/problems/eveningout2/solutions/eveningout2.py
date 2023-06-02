a, b = map(int, input().split())
mini = float('inf')
ans = -1
for i in range(1, int(a**.5)+1):
    if a % i == 0:
        if abs(i - b) < mini:
            mini = abs(i - b)
        if abs(a//i - b) < mini:
            mini = abs(a//i - b)
            if i == 2:break
print(mini)