n, k = map(int, input().split())

sum = 0
for i in range(k):
    sum += int(input())

rem = n - k
maxRem = 3 * (rem)
minRem = -3 * (rem)

print((minRem + sum)/n, (maxRem + sum)/n)