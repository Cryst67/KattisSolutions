n = int(input())
temps = list(map(int, input().split()))
max_temp = float('inf')
day = -1
for i in range(n - 2):
    if max(temps[i], temps[i + 2]) < max_temp:
        day = i + 1
        max_temp = max(temps[i], temps[i + 2])

print(day, max_temp)