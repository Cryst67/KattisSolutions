a, b, c, n = map(int, input().split())
if a >= 1 and b >= 1 and c >= 1 and n>=3 and a+b+c>=n:
    print('YES')
else: print('NO')