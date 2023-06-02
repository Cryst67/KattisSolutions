s, v1, v2 = map(int, input().split())
max_v1 = s//v1
for i in range(s//v1, -1, -1):
    cur = i
    rem = s - v1*i
    if rem % v2 == 0:
        print(cur, rem//v2)
        exit()
else: print('Impossible')