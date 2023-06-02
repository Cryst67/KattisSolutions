n, m = input().split()
index = 1
found = False
while index <= 100:
    if n == m: 
        found = True
        break
    count = [0 for i in range(10)]
    for digit in n:
        count[int(digit)] += 1
    nxt = ''
    for i in range(10):
        if count[i] != 0: nxt += str(count[i]) + str(i)
    n = nxt
    index += 1
if found: print(index)
else: print('Does not appear')
