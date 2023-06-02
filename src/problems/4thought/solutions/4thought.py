cases = ['+', '-', '*', '//']
vals = {}
for a in cases:
    for b in cases:
        for c in cases:
            s = f"4 {a} 4 {b} 4 {c} 4"
            val = eval(s)
            vals[val] = s.replace('//', '/') + f" = {val}"

for i in range(int(input())):
    n = int(input())
    if n not in vals:print('no solution')
    else:print(vals[n])