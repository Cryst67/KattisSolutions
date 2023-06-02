r, c = map(int, input().split())
cheese = r - c
cheese_area = cheese ** 2
print((cheese_area/r ** 2)* 100)
