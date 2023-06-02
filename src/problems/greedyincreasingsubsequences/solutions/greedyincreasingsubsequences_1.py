n=int(input())
l=[*map(int,input().split())]
a,k=[[l[0]]],0
for i in range(1,n):
 if l[i]<=a[k][-1]:a+=[[l[i]]];k += 1
 else:
  for j in range(len(a)):
   if l[i]>a[j][-1]:a[j]+=[l[i]];break
print(len(a))
for i in range(len(a)): print(' '.join(map(str, a[i])))