import decimal 
a, b, c = map(int, input().split())
a = decimal.Decimal(a)
b = decimal.Decimal(b)
c = decimal.Decimal(c)
print(a*b/c)