while True:
    r, c = map(int, input().split())
    if r == c == 0: break
    grid = [list(input()) for _ in range(r)]
    words = ['' for _ in range(c)]
    for i in range(r):
        for j in range(c):
            words[j] += grid[i][j]
    words.sort(key=lambda x: x.lower())
    for i in range(r):
        for j in range(c):
            print(words[j][i], end='')
        print()