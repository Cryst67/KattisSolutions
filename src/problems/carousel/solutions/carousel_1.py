while True:
    n, m = map(int, input().split())
    if n == m == 0: break
    best_val = float('inf')
    t = c = -1
    for _ in range(n):
        a, b = map(int, input().split())
        if a > m: continue
        if b/a == best_val:
            if a > t:
                best_val = b/a
                t, c = a, b
        elif b/a < best_val:
            best_val = b/a
            t, c = a, b
    if best_val == float('inf'): print('No suitable tickets offered')
    else: print(f'Buy {t} tickets for ${c}')
    