for i in range(int(input())):
    print('Test', i + 1)
    r, c = map(int, input().split())
    g = [0 for i in range(r)]
    for i in range(r):
        g[i] = list(input())
    for i in range(r - 1, -1, -1):
        for j in range(c - 1, -1, -1):
            print(g[i][j], end='')
        print()