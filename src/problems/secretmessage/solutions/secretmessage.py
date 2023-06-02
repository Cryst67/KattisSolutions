from math import ceil
for _ in range(int(input())):
    message = input()
    r = c = ceil(len(message) ** .5)
    grid = [['*' for _ in range(c)] for _ in range(r)]
    for i in range(len(message)):
        rr = i//r
        cc = i % c
        grid[rr][cc] = message[i]
    final_str = ''
    for cc in range(c):
        for rr in range(r - 1, -1, -1):
            if grid[rr][cc] == '*': continue
            final_str+= grid[rr][cc]
    print(final_str)