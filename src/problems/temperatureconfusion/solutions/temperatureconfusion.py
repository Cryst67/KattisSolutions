from math import gcd
s = input()
num = 1
den = 1
if s[0] == '-':
    num *= -1
    s=s[1:]
a, b = s.split('/')
num *= int(a)
den *= int(b)
another = 32 * den
num = num - another
num *= 5
den *= 9
d = gcd(num, den)
num = num // d
den = den // d
print(f"{num}/{den}")