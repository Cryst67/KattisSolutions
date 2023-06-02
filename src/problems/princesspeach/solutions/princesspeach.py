n, y = map(int, input().split())
dat = [0 for i in range(n)]
for i in range(y):
    dat[int(input())] = 1
count = 0
for i in range(n):
    if dat[i] != 1:
        print(i)
    else: count += 1

print(f'Mario got {count} of the dangerous obstacles.')