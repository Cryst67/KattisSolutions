N,M,P=map(int,input().split());a=list(map(int,input().split()));h=N;
for i in range(M - 1):
 h-=a[i]
 if h<=a[i+1]:
  while h<=a[i+1] and P!=0:P-=1;h+=20
 if h>N:h=N
if h-a[-1]<=0:print("next time");exit()
print('champion')