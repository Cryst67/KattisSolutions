x, y = map(int, input().split())
if x == 0 and y == 1: print('ALL GOOD')
elif y == 1: print('IMPOSSIBLE')
else: print(-x/(y - 1))