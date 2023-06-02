count = 1
while True:
    n = int(input())
    if n == 0: break
    s = []
    f = [0 for _ in range(n)]
    for i in range(n):
        s.append(input())
    p = 0
    q = len(s) - 1
    for i in range(n):
        if i % 2 == 0:
            f[p] = s[i]
            p += 1
        else:
            f[q] = s[i]
            q -= 1
    print(f"SET {count}")
    for name in f:
        print(name)
    count +=1
        