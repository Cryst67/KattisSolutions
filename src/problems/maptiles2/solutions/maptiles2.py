from math import ceil
n = input()
zoom = len(n)
grid = 2 ** len(n)
x, y = [0, grid - 1], [0, grid - 1]
for num in n:
    num = int(num)
    x_gap = x[1] - x[0]
    y_gap = y[1] - y[0]
    if num == 0:
        x[1] -= ceil(x_gap/2)
        y[1] -= ceil(y_gap/2)
    if num == 1:
        x[0] += ceil(x_gap/2)
        y[1] -= ceil(y_gap/2)
    if num == 2:
        x[1] -= ceil(x_gap/2)
        y[0] += ceil(y_gap/2)
    if num == 3:
        x[0] += ceil(x_gap/2)
        y[0] += ceil(y_gap/2)

print(zoom, x[0], y[0])