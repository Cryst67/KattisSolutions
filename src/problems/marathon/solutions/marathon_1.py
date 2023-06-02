E=5e6
n=int(input())
l=[*map(int, input().split())]
w=max(l[0],E-l[-1])
for i in range(1,n):w=max(w,(l[i]-l[i-1])/2)
c=x=f=0
for i in range(n-1):
 d=l[i+1]-x
 if d > w:
  c+=1;x=l[i]+w
  if E-l[i]<=w:f=1
if not f:c+=1
print(float(w), n-c)