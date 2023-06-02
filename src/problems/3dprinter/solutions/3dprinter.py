n = int(input())
p = 1
days = 0
if n == 1 or n == 2:
    print(n)
    exit()
while True:
    days+=1
    if p >= n:
        break
    p = 2 ** days
print(days)