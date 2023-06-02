for _ in [0]*int(input()):
    g = []
    s = input()
    if len(s)==1:
        print(s)
        continue
    i = 0
    inc = int(len(s) ** .5)
    while i < len(s) - 1:
        a = s[i:i+inc]
        i += inc
        g.append(a)
    o = ''
    for i in range(inc-1, -1, -1):
        for j in range(inc):
            o+=g[j][i]
    print(o)