n = int(input())
d = {}
for i in range(n):
    s = input().split()
    diameter_flag = False
    try:
        r = int(s[0])
        diameter_flag = True
        color = s[1]
    except:
        r = int(s[1])
        color = s[0]
    if diameter_flag: r/=2
    d[color] = r
sd = sorted(d.items(), key = lambda x: float(x[1]))
for key in sd:
    print(key[0])