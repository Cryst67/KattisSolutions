n, w, h = map(int, input().split())
diag = (w ** 2 + h ** 2) ** (1/2)
for i in range(n):
    a = int(input())
    if a <= diag:
        print('DA')
    else:
        print('NE')