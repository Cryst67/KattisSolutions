from functools import reduce
input()
print(abs(reduce(lambda x, y: x + y,list(filter(lambda x: x < 0,list(map(int, input().split())))),0)))