N,M,P=map(int,input().split());a=list(map(int,input().split()));h=N;
for i in range(M):
 h-=a[i]
 if h<=0:print("next time");break
 if i+1==M:print("champion");break
 if h<=a[i+1]:
  while h<=a[i+1] and P!=0:P-=1;h+=20
 if h>N:h=N