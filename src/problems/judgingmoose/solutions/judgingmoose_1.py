l, r = map(int, input().split())
if l == 0 and r == 0:
    print('Not a moose')
elif l == r:
    print(f"Even {l*2}")
else:
    print(f"Odd {max(l,r)*2}")