n,m=input().split()
i=1
while i<101:
 if n==m:print(i);exit()
 t=''
 for j in range(10):
  j=str(j);c=n.count(j)
  if c!=0:t+=str(c)+j
 n=t;i+=1
print('Does not appear')