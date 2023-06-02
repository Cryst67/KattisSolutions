from functools import reduce
g, t, n = map(int, input().split())
w = 0.9 * (g - t)
s = reduce(lambda x, y : x + y, map(int, input().split()), 0)
print(int(w - s))