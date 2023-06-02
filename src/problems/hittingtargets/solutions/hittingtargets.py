from math import dist
m = int(input())
targets = []
for i in range(m):
    targets.append(input().split())

def inside_circle(x,y,r, x1, y1):
    return dist([x, y], [x1, y1]) <= r

def inside_rect(xbl, ybl, xtr, ytr, x1, y1):
    return x1 >= xbl and x1 <=xtr and y1 >= ybl and y1 <= ytr

n = int(input())
for i in range(n):
    x1, y1 = map(int, input().split())
    hits = 0
    for target in targets:
        if target[0] == 'circle':
            x, y, r = map(int, target[1:])
            if inside_circle(x,y,r,x1,y1):
                hits +=1
        if target[0] == 'rectangle':
            xbl, ybl, xtr, ytr = map(int, target[1:])
            if inside_rect(xbl, ybl, xtr, ytr, x1, y1):
                hits += 1
    print(hits)