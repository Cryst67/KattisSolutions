while True:
    line = input()
    if line == '0': break
    k, m = map(int, line.split())
    d = {x : True for x in list(map(int, input().split()))}
    flag = 1
    for _ in range(m):
        line = input().split()
        c, r = map(int, line[:2])
        courses = map(int, line[2:])
        count = 0
        for course in courses:
            if course in d:
                count += 1
        if count < r:
            flag = 0
    if flag: print('yes')
    else: print('no')