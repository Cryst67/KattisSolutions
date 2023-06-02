n = int(input())
tm = ts = 0
for i in range(n):
    m, s = map(int, input().split())
    tm += m
    ts += s
f = ts/(tm*60)
print(f if f > 1 else 'measurement error')