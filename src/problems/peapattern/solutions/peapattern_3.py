n,m=input().split()
for i in range(100):
 if n==m:print(i+1);exit()
 t=''
 for j in range(10):
  c=n.count(str(j))
  if c!=0:t+=str(c)+str(j)
 n=t
print('Does not appear')