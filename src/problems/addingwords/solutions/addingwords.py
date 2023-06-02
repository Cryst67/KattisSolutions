variables = {}
while True:
    try: line = input().split()
    except EOFError: break
    if line[0] == 'def':
        if line[1] in variables:
            variables.pop(variables[line[1]])
        variables[line[1]] = line[2]
        variables[line[2]] = line[1]
    if line[0] == 'clear': variables.clear()
    if line[0] == 'calc':
        f = ''
        unknown_flag = 0
        exp = line[1:len(line) - 1]
        for term in exp:
            if term == '+' or term == '-': f+=term
            else:
                if term not in variables:
                    unknown_flag = 1
                    break
                else: f+=variables[term]
        if unknown_flag:
            print(' '.join(line[1:]), 'unknown')
        else:
            num = str(eval(f))
            if num in variables:
                print(' '.join(line[1:]), variables[num])
            else: print(' '.join(line[1:]), 'unknown')