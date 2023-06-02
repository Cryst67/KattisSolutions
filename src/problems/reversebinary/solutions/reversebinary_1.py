n = int(input())

s = ''
while n != 0:
    if n % 2 == 1:
        s+='1'
    else: s += '0'
    n = int(n/2)

n = 0

for i in range(len(s) -1, -1, -1):
    if s[i] == '1':
        n += pow(2, len(s) - 1 - i)

print(n)
    