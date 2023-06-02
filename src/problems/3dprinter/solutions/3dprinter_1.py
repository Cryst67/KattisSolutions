n = int(input())
p = 1
days = 0
printed = 0
while printed < n:
    if n - printed > p:
        days+=1
        p += p
    else:
        days+=1
        printed += p

print(days)