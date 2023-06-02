#brute force
start, end = map(int, input().split())
count = 0
for i in range(start, end+1):
    cur = set(list(str(i)))
    if len(cur) != 6: continue
    cur = map(int, list(cur))
    flag = True
    for num in cur:
        if num == 0: 
            flag = False
            break 
        if i % num != 0: flag = False
    if flag: count += 1
print(count)