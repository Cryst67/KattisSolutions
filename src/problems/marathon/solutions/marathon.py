END = 5000000
n = int(input())
l = [*map(int, input().split())]

worst = max(l[0], END - l[-1])
for i in range(1, n):
    worst = max(worst, (l[i] - l[i - 1])/2)
print(float(worst), end= ' ')
needed = 0
last = 0
flag = 0
for i in range(n - 1):
    diff = l[i + 1] - last
    if diff > worst:
        needed += 1
        last = l[i] + worst
        if END - l[i] <= worst:
            flag = 1
if not flag: needed += 1
print(n - needed)