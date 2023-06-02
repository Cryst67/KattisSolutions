from functools import reduce
l = int(input())
d = int(input())
x = int(input())

mini = float('inf')
maxi = float('-inf')
for i in range(l, d+1):
    s = reduce(lambda x, y: x + y,list(map(int, list(str(i)))), 0)
    if s == x:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
print(mini)
print(maxi)
