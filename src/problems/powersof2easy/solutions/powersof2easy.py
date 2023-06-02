n, e = map(int, input().split())
num = str(2 ** e)
count = 0
for i in range(1, n + 1):
    if num in str(i): count += 1
print(count)