a = int(input())
l = [input() for _ in range(a)]
b = int(input())
l2= []
d = {}
for i in range(b):
    w = input()
    l2.append(w)
    d[w] = 0
for word in l:
    for i in range(1, len(word) + 1):
        if word[:i] in d:
            d[word[:i]] += 1
for word in l2:
    print(d[word])