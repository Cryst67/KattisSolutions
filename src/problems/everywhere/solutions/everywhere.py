n = int(input())
for i in range(n):
    t = int(input())
    d = {}
    for j in range(t):
        city = input()
        if city not in d:
            d[city] = True
    print(len(d))