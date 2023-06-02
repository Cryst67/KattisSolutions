d = {}
for i in range(int(input())):
    n1, n2, c = input().split()
    n = n1 + n2
    if c not in d:
        d[c] = [1, set([n])]
        continue
    if n in d[c][1]: continue
    else: 
        d[c][0] += 1
        d[c][1].add(n)
keys = sorted(d.keys())
for key in keys:
    print(key, d[key][0])