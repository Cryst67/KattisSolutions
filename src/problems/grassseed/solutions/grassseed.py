c = float(input())
l = int(input())
cost = 0
for i in range(l):
    a, b = map(float, input().split())
    cost += a * b * c
print(cost)
