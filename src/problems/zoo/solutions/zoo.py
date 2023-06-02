count = 1
while True:
    n = int(input())
    if n == 0: break
    d = {}
    for _ in range(n):
        animal = [word.lower() for word in input().split()]
        if animal[-1] in d:
            d[animal[-1]] += 1
        else: d[animal[-1]] = 1
    keys = sorted(d.keys())
    print(f'List {count}:')
    for key in keys:
        print(key, '|', d[key])
    count += 1