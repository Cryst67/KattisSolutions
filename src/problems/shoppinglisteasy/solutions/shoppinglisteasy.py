n, m = map(int, input().split(' '))
collection = []
ingredient_map = {}
for _ in range(n):
    shop_list = set(input().split(' '))
    collection.append(shop_list)
    for ingredient in shop_list:
        if ingredient in ingredient_map:
            ingredient_map[ingredient] += 1
        else:
            ingredient_map[ingredient] = 1
count = 0
commons = []
for key, value in ingredient_map.items():
    if value == n:
        count += 1
        commons.append(key)

print(count)
commons.sort()
for common in commons:
    print(common)