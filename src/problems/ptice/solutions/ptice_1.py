n = int(input())
adrian = 'abc'.upper()
bruno = 'babc'.upper()
goran = 'ccaabb'.upper()
d = {
    'Adrian' : 0,
    'Bruno' : 0,
    'Goran' : 0
}
s = input()
for i in range(n):
    if adrian[i % len(adrian)] == s[i]:
        d['Adrian'] +=1
    if bruno[i % len(bruno)] == s[i]:
        d['Bruno'] += 1
    if goran[i % len(goran)] == s[i]:
        d['Goran'] += 1
maxi = 0
for key in d:
    if d[key] > maxi:
        maxi = d[key]
print(maxi)
for key in d:
    if d[key] == maxi:
        print(key)