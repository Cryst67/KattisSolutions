# N,M,P=map(int,input().split());a=input().split();h=N
# for n in map(int,a):
#  while h<=n and P>0:P-=1;h+=20
#  h=min(n,N)
#  h-=n
# if h<1:print('next time')
# else:print('champion')

import pprint
n = int(input())
l = list(map(int, input().split()))

a = [[l[0]]]
index = 0
for i in range(1, n):
    flag = False
    if l[i] <= a[index][-1]:
        a.append([l[i]])
        Flag = True
        index += 1
    else:
        for j in range(len(a)):
            if l[i] > a[j][-1]:
                a[j].append(l[i])
                flag = True
                break
print(len(a))
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()
