from math import dist
x1, y1, x2, y2, x3, y3, x4, y4 = map(int,input().split())
print(max(dist([x1,y1], [x2,y2]), dist([x3,y3], [x4,y4])))