n=int(input())
c=1
prev = float('-inf')
for i in range(n):
    n=int(input())
    if n < prev:
        c+=1
    prev=n
print(c)