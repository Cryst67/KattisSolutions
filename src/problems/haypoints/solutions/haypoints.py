n, t = map(int, input().split())
d = {}
for _ in range(n):
    s, v = input().split()
    d[s] = int(v)
for _ in range(t):
    f = 0
    words = []
    while True:
        line = input()
        if line == '.': break
        words += line.split()
    for word in words: 
        if word in d:
            f += d[word]
    print(f)