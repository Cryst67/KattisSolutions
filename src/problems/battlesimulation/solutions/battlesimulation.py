import sys
input = sys.stdin.readline
perms = {
    'RBL': 1,
    'RLB': 1,
    'BRL': 1,
    'BLR': 1,
    'LBR': 1, 
    'LRB': 1,
}
s = input()
i = 0
while i < len(s):
    try:
        if s[i:i + 3] in perms:
            print('C', end='')
            i += 3
            continue
    except:
        pass
    if s[i] == 'R':
        print('S', end='')
    if s[i] == 'B':
        print('K', end='')
    if s[i] == 'L':
        print('H', end='')
    i += 1
print()