def g(n):
 if n==0:return['']
 p=g(n-1)
 h=[]
 for s in p:h.append(s+'2');h.append(s+'4')
 return h
n=input()
l=len(n)
a=[]
n=int(n)
while l>=1:a.append(g(l));l-=1
q=[]
for i in range(len(a)):
 for j in range(len(a[i])-1,-1,-1):
  num = int(a[i][j])
  if n % num == 0:q.append(num)
for i in range(len(q)-1,-1,-1):
 print(q[i])