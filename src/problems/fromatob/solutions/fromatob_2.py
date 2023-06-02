a, b = map(int, input().split())
if b >= a: print(b - a)
else:
    count = 0
    while a > b:
        if a % 2 != 0:
            a += 1
            count += 1
        a //= 2
        count += 1
    print(count + (b - a))