try: white = input().split()[1].split(',')
except IndexError: white = []
try: black = input().split()[1].split(',')
except IndexError: black = []
board = [[0 for _ in range(8)] for _ in range(8)]
alphabet = 'abcdefgh'
for piece in white:
    if len(piece) == 2:
        c, r = alphabet.index(piece[0]), 8 - int(piece[1])
        board[r][c] = 'P'
        continue
    k, c, r = piece[0], alphabet.index(piece[1]), 8 - int(piece[2])
    board[r][c] = k
for piece in black:
    if len(piece) == 2:
        c, r = alphabet.index(piece[0]), 8 - int(piece[1])
        board[r][c] = 'p'
        continue
    k, c, r = piece[0], alphabet.index(piece[1]), 8 - int(piece[2])
    board[r][c] = k.lower()
board_row = '+---+---+---+---+---+---+---+---+'
print(board_row)
for i in range(8):
    print('|', end = '')
    for j in range(8):
        final = []
        if i % 2 == 0:
            if j % 2 == 0: final = ['.', '.', '.']
            else: final = [':', ':', ':']
        else:
            if j % 2 == 0: final = [':', ':', ':']
            else: final = ['.', '.', '.']
        if board[i][j] != 0:
            final[1] = board[i][j]
        print(''.join(final), end = '')
        print('|', end = '')
    print()
    print(board_row)