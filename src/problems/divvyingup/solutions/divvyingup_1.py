from functools import reduce
n = int(input())
num = reduce(lambda x, y: x+y,list(map(int, input().split())),0)
if (num/3).is_integer():
    print('yes')
else:
    print('no')