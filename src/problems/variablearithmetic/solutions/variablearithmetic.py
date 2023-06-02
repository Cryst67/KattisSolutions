variables = {}
while True:
    line = input()
    if line == '0': break
    line = line.split()
    if line.count('='): variables[line[0]] = int(line[2]); continue
    f = 0
    rem = []
    for term in line:
        if term == '+': continue
        try: 
            term = int(term)
            f += term
        except ValueError:
            if term in variables:
                f += variables[term]
            else: rem.append(term)
    s = ''
    for i in range(len(rem)):
        if i == len(rem) - 1: s += rem[i]
        else: s += rem[i] + ' + '
    if f != 0 and s == '':
        print(f)
    elif f == 0 and s != '': print(s)
    else: print(f'{f} + {s}')
