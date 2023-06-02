d = {}
f = True
while True:
    try: s = input()
    except EOFError: break
    if s == '': 
        f = False
        continue
    if f: 
        eng, frn = s.split()
        d[frn] = eng
        continue
    if s in d:
        print(d[s])
    else: print('eh')