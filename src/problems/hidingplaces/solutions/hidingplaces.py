#basic bfs
n = int(input())
alpha_cols = 'abcdefgh'
cols = {alpha_cols[i]: i for i in range(8)}
def get_coordinates(s): return (8 - int(s[1]), cols[s[0]])
def get_chess_coord(t): return alpha_cols[t[1]] + str(8 - t[0])
def update(grid, queue, coordinates):
    r, c = coordinates
    moves = grid[r][c]
    inf = float('inf')
    updates = 0
    if r - 2 > -1:
        if c - 1 > -1 and grid[r - 2][c - 1] == inf: 
            queue.append((r - 2, c - 1))
            grid[r - 2][c - 1] = moves + 1
        if c + 1 < 8 and grid[r - 2][c + 1] == inf:
            queue.append((r - 2, c + 1))
            grid[r - 2][c + 1] = moves + 1
    if c - 2 > -1:
        if r - 1 > -1 and grid[r - 1][c - 2] == inf:
            queue.append((r - 1, c - 2))
            grid[r - 1][c - 2] = moves + 1
        if r + 1 < 8 and grid[r + 1][c - 2] == inf:
            queue.append((r + 1, c - 2))
            grid[r + 1][c - 2] = moves + 1
    if c + 2 < 8:
        if r - 1 > -1 and grid[r - 1][c + 2] == inf:
            queue.append((r - 1, c + 2))
            grid[r - 1][c + 2] = moves + 1
        if r + 1 < 8 and grid[r + 1][c + 2] == inf:
            queue.append((r + 1, c + 2))
            grid[r + 1][c + 2] = moves + 1
    if r + 2 < 8:
        if c - 1 > -1 and grid[r + 2][c - 1] == inf: 
            queue.append((r + 2, c - 1))
            grid[r + 2][c - 1] = moves + 1
        if c + 1 < 8 and grid[r + 2][c + 1] == inf:
            queue.append((r + 2, c + 1))
            grid[r + 2][c + 1] = moves + 1
    return grid, queue, moves + 1
    
def custom_sort(array, n):
    for i in range(n-1):
        for j in range(n - 1):
            item1 = array[j]
            item2 = array[j+1]
            if int(item1[1]) == int(item2[1]):
                if item1[0] > item2[0]:
                    array[j] = item2
                    array[j + 1] = item1
            elif int(item1[1]) < int(item2[1]):
                    array[j] = item2
                    array[j + 1] = item1
    return array

for _ in range(n):
    start = input()
    r, c = get_coordinates(start)
    grid = [[float('inf') for i in range(8)] for i in range(8)]
    grid[r][c] = 0
    move = 0
    queue = [get_coordinates(start)]
    move_dict = {0: [get_chess_coord((r, c))]}
    while queue:
        r, c = queue.pop(0)
        moves = grid[r][c]
        if moves not in move_dict: move_dict[moves] = [get_chess_coord((r, c))]
        else: move_dict[moves].append(get_chess_coord((r, c)))
        grid, queue, move = update(grid, queue, (r, c))
    if move not in move_dict: move -= 1
    print(move, end = ' ')
    final = custom_sort(move_dict[move], len(move_dict[move]))
    for coord in final: print(coord, end = ' ')
    print()