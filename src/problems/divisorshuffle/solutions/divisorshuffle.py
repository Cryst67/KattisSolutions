n = int(input())
l = sorted(list(map(int, (input().split()))))
if n == 1:
    print(1, 1)
    exit()
if n == 2:
    print(1, max(l))
    exit()
seen = set()
maxi = l[-1]
mini = float('inf')
for i in range(len(l)-1,-1,-1):
    if maxi % l[i] != 0:
        mini = l[i]
        break
    elif maxi % l[i] == 0 and l[i] in seen:
        mini = l[i]
        break
    seen.add(l[i])
print(mini, maxi)