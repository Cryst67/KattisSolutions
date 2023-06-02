lines = []
seen = {}
while True:
    try: line = input().split()
    except EOFError: break
    for i in range(len(line)):
        if line[i].lower() in seen:
            line[i] = '.'
        else: seen[line[i].lower()] = 1
    print(' '.join(line))