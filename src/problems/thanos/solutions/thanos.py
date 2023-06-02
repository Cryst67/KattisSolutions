for i in range(int(input())):
    p, r, f = map(int, input().split())
    count = 0
    while p <= f:
        p*= r
        count += 1
    print(count)