from math import factorial as f
a=int(input())
n=9
s=''
if a==1:print(0);exit()
while a!=0:
 if f(n)<=a:a-=f(n);s+=str(n)
 else:n-=1
print(s[::-1])