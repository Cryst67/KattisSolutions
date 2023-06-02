a, b, c = map(int, input().split())
if (b - a) * (c - b) < 0:
    print('turned')
elif abs(c - b) > abs(b - a):
    print('accelerated')
elif abs(c - b) < abs(b - a):
    print('braked')
else:
    print('cruised')