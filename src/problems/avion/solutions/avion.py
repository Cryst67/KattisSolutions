a = []
for i in range(5):
    s = input()
    for j in range(len(s)):
        if j == len(s) - 2:
            break
        if s[j] == 'F' and s[j+1]=='B' and s[j+2]=='I':
            a.append(i + 1)
if len(a) == 0:
    print('HE GOT AWAY!')
    exit()
for n in a:
    print(n, end= ' ')
print()