n = input()
m = input()
res = []
i = 0
j = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while i != len(n) or j != len(m):
    if i == len(n) and j!= len(m):
        res.append(m[j])
        j+=1
        continue
    if i != len(n) and j== len(m):
        res.append(n[i])
        i+=1
        continue
    if alphabet.index(n[i]) < alphabet.index(m[j]):
        res.append(n[i])
        i+=1
    elif alphabet.index(n[i]) == alphabet.index(m[j]):
        res.append(n[i])
        res.append(m[j])
        i+=1
        j+=1
    else:
        res.append(m[j])
        j+=1
s = ''
for l in res:
    s+=l
print(s)