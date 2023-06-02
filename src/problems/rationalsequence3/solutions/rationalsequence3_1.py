for _ in range(int(input())):
    k, n = map(int, input().split())
    n-=1
    l = []
    while n != 0:
        l += [n]
        n = (n - 1)//2
    l.append(0)
    p,q=1,1
    for i in range(len(l) - 2, -1, -1):
        if l[i] == (2*l[i+1])+1:
            p,q = p, p+q
        else: p,q = p+q, q
    print(k, f'{p}/{q}')