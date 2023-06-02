while True:
    t = int(input())
    if t == 0: break
    d = {}  
    s = set()
    for i in range(t):
        line = input().split()
        name, order = line[0], line[1:]
        for item in order:
            if item not in d:
                d[item] = [name]
            else: d[item].append(name)
            s.add(item)
    s = list(s)
    s.sort()
    for key in s:
        l = d[key]
        l.sort()
        print(f"{key} {' '.join(l)}")
    print()