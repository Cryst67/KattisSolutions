n = int(input())
l = []
for i in range(n): l.append(input())
if sorted(l) == l:
    print('INCREASING')
elif sorted(l, reverse=True) == l:
    print('DECREASING')
else:print('NEITHER')
