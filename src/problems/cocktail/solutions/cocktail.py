n, t = map(int, input().split())
potions = []
for i in range(n):
    potions.append(int(input()))
potions.sort(reverse = 1)
if n == 0: print('NO')
time_elapsed = 0
for i in range(1, n):
    time_elapsed += t
    if time_elapsed >= potions[0]: print('NO'); exit()
print('YES')