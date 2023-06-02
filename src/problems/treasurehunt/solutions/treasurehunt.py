from pprint import pprint
r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
rr, cc, moves = 0, 0, 0
lost = out = 0
while True:
    if (rr < 0 or rr > r - 1) or (cc < 0 or cc > c - 1):
        out = 1; break
    if visited[rr][cc]:
        lost = 1; break
    if grid[rr][cc] == 'T':
        break
    visited[rr][cc] = 1
    if grid[rr][cc] == 'N':
        rr -= 1
    elif grid[rr][cc] == 'S':
        rr += 1
    elif grid[rr][cc] == 'W':
        cc -= 1
    elif grid[rr][cc] == 'E':
        cc += 1
    moves += 1

if out: print('Out')
elif lost: print('Lost')
else: print(moves)