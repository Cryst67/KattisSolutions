n, p = map(int, input().split())
grades = list(map(int, input().split()))
s = sum(grades)
avg = s/n
c = 0 
if p == 100: print('impossible');exit()
while avg < p:
    s += 100
    n += 1
    c += 1
    avg = s/n
print(c)