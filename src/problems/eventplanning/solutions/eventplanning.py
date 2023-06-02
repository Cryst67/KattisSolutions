n, b, h, w = map(int, input().split())
cheapest = float('inf')
for i in range(h):
    price = int(input())
    weeks = list(map(int, input().split()))
    for available in weeks:
        if available >= n:
            if n * price <= b:
                cheapest = min(cheapest, n*price)
print(cheapest if cheapest != float('inf') else 'stay home')