n = int(input())

base = 1
blocks = 1
l = 1
while blocks < n:
    base += 2
    blocks += base * base
    if blocks <= n:
        l += 1
print(l)