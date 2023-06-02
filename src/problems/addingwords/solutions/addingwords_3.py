import sys
lines = sys.stdin.readlines()

variables = {}

def calc(line,data):
    temp = ''
    for i in line:
        if i!='+' and i!='-' and i!='=':
            if data.get(i)!=None:
                temp+=data.get(i)
            else:
                return "unknown"
        else:
            temp+=i
    inv_mapping = {v:k for k,v in data.items()}
    final = inv_mapping.get(str(eval(temp[:-1])))
    if final == None:
        return "unknown"
    else:
        return final

for line in lines:
    line = line.split()
    if line[0] == 'def':
        variables[line[1]] = line[2]
        variables[line[2]] = line[1]
    elif line[0] == 'calc':
        print(' '.join(line[1:]), calc(line[1:], variables))
    elif line[0] == 'clear':
        variables = {}