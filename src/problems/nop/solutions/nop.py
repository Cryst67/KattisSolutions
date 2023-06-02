s = input()
d = []
for i in range(len(s)):
    if s[i].isupper():  
        d.append(i)
f = 0
for i in range(len(d) - 1):
    diff = d[i + 1] - d[i]
    if diff % 4 == 0: continue
    f += abs(4 - (diff % 4))
print(f)