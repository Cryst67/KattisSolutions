n,m=input().split()
i=1
while i<=100:
 if n==m:print(i);exit()
 c=[0]*10
 for d in n:c[int(d)]+=1
 t=''
 for j in range(10):
  if c[j]!=0:t+=str(c[j])+str(j)
 n=t;i+=1
print('Does not appear')