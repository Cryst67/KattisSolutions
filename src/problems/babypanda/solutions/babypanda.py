from math import log2
a, b = map(int, input().split())
c = 1
if b == 0:
    print(0)
    exit()
while not log2(b).is_integer():
    b -= 2 ** int(log2(b))
    c+=1
print(c)