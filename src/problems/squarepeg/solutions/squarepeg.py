l, r = map(int, input().split())
print('fits' if (2**.5)*l <= r*2 else 'nope')