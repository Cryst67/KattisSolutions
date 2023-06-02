n = list(input())
m = list(input())
while n[-1] == m[-1] == '0':
    n.pop(); m.pop()
if len(m) > len(n):
    print('0.', end='')
    for i in range(len(m) - len(n) - 1):
        print('0', end='')
    print(''.join(n))
else:
    print(''.join(n[:len(n) - len(m) + 1]), end='')
    if len(n) - len(m) + 1 < len(n): print('.' + ''.join(n[len(n) - len(m) + 1:]))