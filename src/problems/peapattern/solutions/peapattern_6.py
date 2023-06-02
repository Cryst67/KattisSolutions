n,m=input().split()
i=1
while i<=100:
 if n==m:print(i);exit()
 c=[0 for _ in range(10)]
 for digit in n:c[int(digit)]+=1
 t=''
 for j in range(10):
  if c[j]!=0:t+=str(c[j])+str(j)
 n=t;i+=1
print('Does not appear')