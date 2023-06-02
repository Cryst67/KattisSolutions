c, x, m = map(float, input().split())

d = []
for i in range(6):
    d.append(list(map(float, input().split())))
d.sort(key = lambda x: x[0])
for i in range(5, -1, -1):
    gallons = c/2
    hours = m/d[i][0]
    gallons -= x * hours
    if d[i][1] * gallons > m:
        print('YES', int(d[i][0]))
        exit()
print('NO')