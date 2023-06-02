ds, ys = map(int, input().split())
dm, ym = map(int, input().split())


y = 1
while y < 5001:
    if (y + dm) % ym == 0 and (y + ds) % ys == 0:
        print(y)
        break
    y += 1
