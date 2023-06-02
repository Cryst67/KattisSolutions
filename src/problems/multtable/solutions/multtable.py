n,m=map(int,input().split())
c=0
for i in range(1,int(m**.5)+2):
 if m%i==0:
  a,b=i,m//i
  if a<=n and b<=n:
   if a==b:c+=1
   else:c+=2
print(c)