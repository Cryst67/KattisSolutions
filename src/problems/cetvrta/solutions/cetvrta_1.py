x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

xs = [x1, x2, x3]
ys = [y1, y2, y3]
set_x = set(xs)
set_y = set(ys)
for x in set_x:
    if xs.count(x) == 1:
        for y in set_y:
            if ys.count(y) == 1:
                print(x, y)
                exit()