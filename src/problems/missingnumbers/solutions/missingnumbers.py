n = int(input())
d = {i + 1 : False for i in range(200)}
last = -1
for i in range(n):
    num = int(input())
    d[num] = True
    last = num
flag = False
for key in d:
    if key == last:
        break
    if not d[key]:
        flag = True
        print(key)

if not flag:
    print('good job')