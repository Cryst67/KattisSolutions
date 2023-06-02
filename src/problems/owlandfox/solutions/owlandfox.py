for i in range(int(input())):
    n = int(input())
    get_sum = lambda n: sum(list(map(int, list(str(n)))))
    sm = get_sum(n)
    if sm == 1:
        print(0)
        continue
    for i in range(n - 1, -1, -1):
        if get_sum(i) + 1  == sm:
            print(i)
            break