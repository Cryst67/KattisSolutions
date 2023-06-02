a,b=map(int,input().split())
m=10e15
for i in range(1,int(a**.5)+1):
 if a%i==0:m=min(m,abs(i-b),abs(a//i-b))
print(m)