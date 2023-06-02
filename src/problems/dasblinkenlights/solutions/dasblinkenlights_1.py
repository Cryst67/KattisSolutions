from math import gcd
a, b, c = map(int,input().split())
print('yes' if abs(a*b)//gcd(a,b) <= c else 'no')