a, b ,c = map(int, input().split())
for _ in [0]*c:
    l = list(map(int, input().split()))[1:]
    if b in l:
        print('KEEP')
    else: print('REMOVE')