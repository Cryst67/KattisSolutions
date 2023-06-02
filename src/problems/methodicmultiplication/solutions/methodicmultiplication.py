s1 = input()
s2 = input()

prod = s1.count('S') * s2.count('S')
a = '0'
for i in range(prod):
    a = 'S(' + a + ')'
print(a) 