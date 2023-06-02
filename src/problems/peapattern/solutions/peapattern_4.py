n,m=input().split()
for i in range(100):
 if n==m:print(i+1);exit()
 t=''
 for j in range(10):
  if n.count(str(j))!=0:t+=str(n.count(str(j)))+str(j)
 n=t
print('Does not appear')