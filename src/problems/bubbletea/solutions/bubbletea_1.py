tea_count = int(input())
teas = list(map(int, input().split()))
topping_count = int(input())
toppings = list(map(int, input().split()))
min_cost = float('inf')
for i in range(tea_count):
    l = list(map(int, input().split()))[1:]
    for num in l:
        min_cost = min(teas[i] + toppings[num - 1], min_cost)

print(max(0, int(input())//min_cost - 1))