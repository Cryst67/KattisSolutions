import sys
lines = sys.stdin.readlines()

variables = {}
for line in lines:
    line = line.split()
    if line[0] == 'def':
        variables[line[1]] = line[2]
    elif line[0] == 'calc':
        f = ''
        flag = 1
        for i in line[1:]:
            if i == '+' or i == '-' or i == '=': f += i
            else:
                if i in variables:
                    f += variables[i]
                else:
                    print(' '.join(line[1:]), 'unknown')
                    flag = 0
                    break
        if flag:
            inv = {v: k for k, v in variables.items()}
            final = inv.get(str(eval(f[:-1])))
            if final == None:
                print(' '.join(line[1:]), 'unknown')
            else:
                print(' '.join(line[1:]), final)
    elif line[0] == 'clear':
        variables = {}