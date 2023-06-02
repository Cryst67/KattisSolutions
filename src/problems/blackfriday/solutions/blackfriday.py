n=int(input())
l=list(map(int, input().split()))
d = {i:[] for i in range(1, 7)}

for i in range(n):
    d[l[i]].append(i + 1)

maxi = -1
for key in d:
    if len(d[key]) == 1 and key > maxi:
        maxi = key
if maxi == -1:
    print('none')
    exit()
print(d[maxi][0])