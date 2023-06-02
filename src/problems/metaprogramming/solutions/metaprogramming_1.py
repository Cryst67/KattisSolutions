d = {}
while True:
    try: line = input().split()
    except EOFError: break
    if line[0] == 'define':
        d[line[2]] = int(line[1])
    if line[0] == 'eval':
        v1 = line[1]
        cmp = line[2]
        v2 = line[3]
        if cmp == '<':
            try: print('true' if d[v1] < d[v2] else 'false')
            except: print('undefined')
        if cmp == '>':
            try: print('true' if d[v1] > d[v2] else 'false')
            except: print('undefined')
        if cmp == '=':
            try: print('true' if d[v1] == d[v2] else 'false')
            except: print('undefined')