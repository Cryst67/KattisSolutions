for _ in range(int(input())):
    d = {}
    n = int(input())
    for i in range(n):
        name, amt = input().split()
        if name in d: d[name] += int(amt)
        else: d[name] = int(amt)
    keys = sorted(list(d.keys()), key=lambda x: (-d[x], x))
    print(len(keys))
    for key in keys:
        print(key, d[key])