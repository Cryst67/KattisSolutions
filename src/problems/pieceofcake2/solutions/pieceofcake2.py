n, h, v = map(int, input().split())

x = max(n-h, h)
y = max(n-v, v)
print(x*y*4)