alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
s = input()
a = s[0:len(s)//2]
b = s[len(s)//2:]
ra = 0
rb = 0
for i in range(len(s)//2):
    ra += alphabet.index(a[i])
    rb += alphabet.index(b[i])
c = ''
d = ''
for i in range(len(s)//2):
    r1 = alphabet.index(a[i]) + ra
    r2 = alphabet.index(b[i]) + rb
    if r1 > 26:r1 = r1 % 26
    if r2 > 26:r2 = r2 % 26
    c += alphabet[r1]
    d += alphabet[r2]
o = ''
for i in range(len(s)//2):
    n = alphabet.index(c[i]) + alphabet.index(d[i])
    if n > 25: n= n % 26
    o+=alphabet[n]
print(o)
