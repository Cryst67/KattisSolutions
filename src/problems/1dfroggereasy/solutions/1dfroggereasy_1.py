n, new_index, m = map(int, input().split())
l = [0, *map(int, input().split())]
visited = [0 for i in range(n + 1)]
moves = 0
while True:
    if new_index < 1: print(f'left\n{moves}');break
    elif new_index > n: print(f'right\n{moves}');break
    if l[new_index] == m: print(f'magic\n{moves}'); break
    if visited[new_index]:
        print(f'cycle\n{moves}');break
    else:
        visited[new_index] = 1
        new_index += l[new_index]
        moves += 1