while True:
    p, q = map(int, input().split())
    if p == 0 and q == 0:
        break
    print(f"{p // q} {p%q} / {q}")
