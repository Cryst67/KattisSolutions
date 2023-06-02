n, m = map(int, input().split())

d = {}

for _ in range(m):
    a, b = map(int, input().split())
    if a not in d:
        d[a] = 1
    else: d[a] +=1
    if b not in d:
        d[b] = -1
    else: d[b] -= 1

start = 0
end = 0
startFlag = 0
endFlag = 0
for key in d:
    if d[key] == 0:
        continue
    if d[key] == -1:
        if not endFlag:
            end = key
            endFlag = 1
        else:
            print('no')
            exit()
    if d[key] > 1 or d[key] < -1:
        print('no')
        exit()
    if d[key] == 1:
        if not startFlag:
            start = key
            startFlag = 1
        else:
            print('no')
            exit()

if not startFlag and not endFlag:
    print('anywhere')
    exit()
    
print(start, end)