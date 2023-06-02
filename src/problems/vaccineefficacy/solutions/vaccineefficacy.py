n = int(input())
d = {
    'N': {
        'count': 0,
        'A': 0,
        'B': 0,
        'C': 0
    },
    'Y': {
        'count': 0,
        'A': 0,
        'B': 0,
        'C': 0
    }
}

for i in range(n):
    group, a, b, c = list(input())
    d[group]['count'] += 1
    if a == 'Y': d[group]['A'] += 1
    if b == 'Y': d[group]['B'] += 1
    if c == 'Y': d[group]['C'] += 1

control, ctrl_n = d['N'], d['N']['count']
experiment, exp_n = d['Y'], d['Y']['count']
ctrl_a = control['A']/ctrl_n
ctrl_b = control['B']/ctrl_n
ctrl_c = control['C']/ctrl_n
exp_a = experiment['A']/exp_n
exp_b = experiment['B']/exp_n
exp_c = experiment['C']/exp_n
if exp_a >= ctrl_a: print('Not Effective')
else: 
    print((1 - exp_a/ctrl_a)*100)
if exp_b >= ctrl_b: print('Not Effective')
else:
    print((1 - exp_b/ctrl_b)*100)
if exp_c >= ctrl_c: print('Not Effective')
else:
    print((1 - exp_c/ctrl_c)*100)