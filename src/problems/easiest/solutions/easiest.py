from functools import reduce
while True:
    n = input()
    if n == '0':
        break
    summ = reduce(lambda x,y: x+y, list(map(int, list(n))))
    times = 11
    while True:
        if summ == reduce(lambda x,y: x+y, list(map(int, str(int(n) * times)))):
            print(times)
            break
        times+=1