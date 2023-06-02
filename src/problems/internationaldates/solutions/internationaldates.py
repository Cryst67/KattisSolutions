a, b, c = map(int, input().split('/'))
if a < 13 and b > 12: print('US')
elif a > 12 and b < 13: print('EU')
else:print('either')