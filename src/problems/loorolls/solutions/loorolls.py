l, n = map(int, input().split())
i=1
result = l%n
while result != 0:
    i+=1
    n-=result
    result =l%n
print(i)