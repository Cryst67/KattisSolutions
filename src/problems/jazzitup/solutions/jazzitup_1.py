n = int(input())
m = 2
found = False
ans = 0
while m < n:
    k = 2
    found = False
    while k**2 < m * n:
        if (m * n) % k**2 == 0:
            found = True
            break
        k+=1
    if not found: break
    m +=1
print(m)