from heapq import heappop as q, heappush as p
import sys
l,h1,h2,n,r,a=sys.stdin.readlines(),[],[],0,print,len
for s in l:
 if s=='#\n':
  if n%2!=0:r(-1*q(h1))
  else:r(q(h2))
  n-=1
  if n<0:n=0
  continue
 s=int(s);n+=1
 if a(h1)==0:p(h1,-1*s);continue
 if a(h2)==0:
  m=q(h1)
  if-1*m>=s:p(h2,-1*m);p(h1,-1*s)
  else:p(h2,s);p(h1,m)
  continue
 m=q(h1);k=q(h2)
 if s<=-1*m:p(h1,-1*s)
 else:p(h2,s)
 p(h1,m);p(h2,k)
 if a(h2)>a(h1):k=q(h2);p(h1,-1*k)
 if a(h1)>a(h2)+1:p(h2,-q(h1))