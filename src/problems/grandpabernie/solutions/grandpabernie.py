n = int(input())
d = {}
for i in range(n):
    place, year = input().split()
    year = int(year)
    if place in d:
        d[place] += [year]
    else: d[place] = [year]

for key in d:
    l = d[key]
    l.sort()
    d[key] = l
q = int(input())
for i in range(q):
    place, index = input().split()
    index = int(index)
    print(d[place][index - 1])