n = 0
d = {}
l = []
while True:
    try:
        s = input()
    except EOFError:
        break
    if s in d:
        d[s] +=1
    else: 
        d[s] = 1
    n+=1
    l.append(s)
l = list(set(l))
l.sort()
for tree in l:
    print(tree, (d[tree]/n)*100)