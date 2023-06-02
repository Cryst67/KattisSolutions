while True:
    try: line = list(map(int, input().split()))
    except EOFError: break
    n = line[0]
    l = line[1:]
    final = [0 for i in range(n)]
    jolly = True
    for i in range(n - 1):
        diff = abs(l[i] - l[i + 1])
        if diff < 1 or diff > n - 1:
            jolly = False
        else: 
            if final[diff]: jolly = False
            else: final[diff] = 1
    print('Jolly' if jolly else 'Not jolly')