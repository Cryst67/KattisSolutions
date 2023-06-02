while True:
    n = int(input())
    if n == 0: break
    d = {}
    for i in range(n):
        s = input()
        if s[0:2] in d:
            d[s[0:2]].append(s)
        else:
            d[s[0:2]] = [s]
    for key in sorted(d.keys()):
        for name in d[key]:
            print(name)
    print()