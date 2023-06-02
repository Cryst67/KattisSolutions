n = int(input())
sum = 0
for i in range(n):
    x, y = map(float,input().split())
    sum +=  x*y

print(sum)
