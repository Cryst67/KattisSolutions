n,m=map(int, input().split())
l=[*map(int, input().split())]
c,e = 0,0
for i in range(m):
 if l[i]%2==0:e+=1
if e>1:c+=1
for i in range(1,n-(m-1)):
 if l[i-1]%2==0:e-=1
 if l[i+(m-1)]%2==0:e+=1
 if e>1:c+=1
print(c)