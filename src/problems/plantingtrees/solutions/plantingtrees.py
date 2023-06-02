n = int(input())
l = sorted([*map(int, input().split())], reverse=1)
days = 1
days_to_wait = l[0]
for i in range(1, n):
    days_to_wait = max(days_to_wait - 1, l[i])
    days += 1
print(days + days_to_wait + 1)