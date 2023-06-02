while True:
    try: m, p, l, e, r, s, n = map(int, input().split())
    except EOFError: break
    for i in range(n):
        pm,pp,pl = m,p,l
        l = pm*e
        p = pl//r
        m = pp//s
    print(m)