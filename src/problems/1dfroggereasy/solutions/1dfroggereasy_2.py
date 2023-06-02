n, index, m = map(int, input().split())
l = [0, *map(int, input().split())]
visited = [0 for _ in range(n + 1)]
moves = 0
while True:
    if index < 1: print(f'left\n{moves}'); break
    if index > n: print(f'right\n{moves}'); break
    if l[index] == m: print(f'magic\n{moves}'); break
    if visited[index]: print(f'cycle\n{moves}');break
    else:
        visited[index] = 1
        index += l[index]
        moves += 1