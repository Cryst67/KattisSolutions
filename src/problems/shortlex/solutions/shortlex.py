a=["0","1"]
for _ in[0]*int(input()):
 n=int(input());s=''
 while n>0:i=(n-1)%2;s=a[i]+s;n=(n-1)//2
 print(s)