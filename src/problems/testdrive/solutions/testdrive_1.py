a, b, c = map(int, input().split())
if b - a > 0 and c - b < 0 or b - a < 0 and c - b > 0:
    print('turned')
elif abs(c - b) > abs(b - a):
    print('accelerated')
elif abs(c - b) < abs(b - a):
    print('braked')
elif c - b == b - a:
    print('cruised')