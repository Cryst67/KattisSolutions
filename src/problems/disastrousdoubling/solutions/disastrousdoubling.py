n = int(input())
l = list(map(int, input().split()))
start = 1
mod = int(1e9) + 7
for i in range(n):
    start = start * 2
    if start - l[i] < 0: print('error'); exit()
    start -= l[i]
print(start % mod)