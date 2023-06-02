n = int(input())
v = 7
for i in range(n):
    s = input()
    if s == 'Skru op!':
        v += 1
        v = min(v, 10)
    elif s == 'Skru ned!':
        v -= 1
        v = max(v, 0)

print(v)
    