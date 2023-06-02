n = int(input())
bb = input().split()
if bb[0] == 'mumble':
    bb[0] = 1
bb[0] = int(bb[0])
for i in range(1, n):
    if bb[i] == 'mumble': bb[i] = int(bb[i - 1]) + 1
    bb[i] = int(bb[i])
actual = [i + 1 for i in range(n)]
print('makes sense' if bb == actual else 'something is fishy')