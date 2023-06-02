d = {
    'c': ['number of', 'most', 'fewest', 'more', 'fewer', 'many', 'few'],
    'm': ['amount of', 'most', 'least', 'more', 'less', 'much', 'little']
}

n, p = map(int, input().split())
d2 = {}
for i in range(n):
    a, b = input().split()
    d2[a] = b

for i in range(p):
    s = input().split()
    noun = s[-1]
    phrase = ' '.join(s[:-1])
    if phrase in d[d2[noun]]:
        print('Correct!')
    else: print('Not on my watch!')