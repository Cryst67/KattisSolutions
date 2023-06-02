p, n = map(int, input().split())
s = set()
day = 0
all_fix = False
for i in range(n):
    s.add(input())
    if len(s) == p and not all_fix:
        day = i + 1
        all_fix = True
if day == 0:
    print('paradox avoided')
else:
    print(day)