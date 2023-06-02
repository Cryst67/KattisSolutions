h, w, n = map(int, input().split())
bricks = map(int, input().split())
cur_width = 0
cur_height = 0
for brick in bricks:
    if cur_height == h:
        print('YES')
        exit()
    cur_width += brick
    if cur_width == w:
        cur_height += 1
        cur_width = 0
    elif cur_width > w:
        print('NO')
        exit()
if cur_height == h:
    print('YES')
else: print('NO')