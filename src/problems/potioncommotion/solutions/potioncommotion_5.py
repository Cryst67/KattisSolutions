N,M,P=map(int,input().split());a=list(map(int,input().split()));h=N;p=P
for i in range(M):
 h-=a[i]
 if h<=0:print("next time");exit()
 if i+1==M:print("champion");exit()
 if h<=a[i+1]:
  while h<=a[i+1] and p!=0:p-=1;h+=20
 if h>N:h=N