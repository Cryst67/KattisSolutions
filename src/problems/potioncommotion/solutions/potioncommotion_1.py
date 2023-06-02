N,M,P=map(int,input().split());a=list(map(int,input().split()));h=N
for n in a:
 while h<=n and P!=0:P-=1;h+=20
 if h>N:h=N
 h-=n
if h<=0:print('next time');exit()
print('champion')