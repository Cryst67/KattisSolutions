n,f=int(input()),[]
for i in range(n):
 f+=[[*map(int,input().split())]]
m,mi=0,[]
for i in range(n):
 for j in range(i+1,n):
  for k in range(j+1,n):
   s=f[i][j]*f[i][k]*f[j][k]
   if s>m:m=s;mi=[i+1,j+1,k+1]
print(' '.join(map(str,mi)))