n=int(input())
p=list(map(int,input().split()))
g={i+1:n for i,n in enumerate(p)}
for _ in [0]*int(input()):
 a,b=map(int,input().split());g[a]+=p[b-1];g[b]+=p[a-1]
c=float('inf');d=-1
for k in g:
 if g[k] < c:c = g[k];d = k
print(d)