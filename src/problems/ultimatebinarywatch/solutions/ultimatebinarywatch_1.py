n = input()
w = [0 for _ in range(4)]
for i in range(4):
    b = bin(int(n[i]))[2:]
    while len(b) < 4:
        b = '0' + b
    b = list(b)
    for j in range(4):
        if b[j] == '0': b[j] = '.'
        else: b[j] = '*'
    w[i] = b
for i in range(4):
    for j in range(4):
        if j == 1:
            print(w[j][i], end = '   ')
        else:
            if j == 3:
                print(w[j][i], end = '')
            else:print(w[j][i], end=' ')
    print()