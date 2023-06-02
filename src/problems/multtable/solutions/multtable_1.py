n, m = map(int, input().split())
count = 0
for i in range(1, int(m ** .5) + 2):
    if m % i == 0:
        a, b = i, m//i
        if a <= n and b <= n:
            if a == b:
                count+=1
                continue
            count+=2
print(count)

