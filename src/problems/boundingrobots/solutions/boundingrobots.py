while True:
    w, l = map(int, input().split())
    if w == l == 0: break
    w -= 1; l -= 1
    rx = ry = 0
    x = y = 0
    for _ in range(int(input())):
        direction, steps = input().split()
        steps = int(steps)
        if direction == 'u': ry += steps; y += steps; y = min(l, y)
        if direction == 'r': rx += steps; x += steps; x = min(w, x)
        if direction == 'd': ry -= steps; y -= steps; y = max(0, y)
        if direction == 'l': rx -= steps; x -= steps; x = max(0, x)
    print(f'Robot thinks {rx} {ry}')
    print(f'Actually at {x} {y}')
