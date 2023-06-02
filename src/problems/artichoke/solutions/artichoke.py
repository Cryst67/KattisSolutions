from math import sin, cos
p, a, b, c, d, n = map(int, input().split())
prices = [(p * (sin(a*(i+1) + b) + cos(c*(i+1) + d) + 2)) for i in range(n)]
l = [0]
max_dif = 0
max_val = prices[0]
for i in range(n - 1):
    if max_val < prices[i + 1]: max_val = prices[i + 1]
    elif max_val - prices[i + 1] > max_dif: max_dif = max_val - prices[i + 1]
print(max_dif)