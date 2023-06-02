k, r = map(int, input().split())
ingredient_supply = list(map(int, input().split()))
max_profit = float('-inf')
for _ in range(r):
    supply = ingredient_supply.copy()
    l = list(map(int, input().split()))
    ingredients_used = l[:-1]
    price = l[-1]
    bottleneck = float('inf')
    for i in range(k):
        if ingredients_used[i] == 0: continue
        bottleneck = min(bottleneck, supply[i]//ingredients_used[i])
    max_profit = max(price * bottleneck, max_profit)
print(max_profit)