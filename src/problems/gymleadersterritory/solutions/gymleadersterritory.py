n,k,m=map(int,input().split())
g={i+1:[]for i in range(n)}
for i in [0]*m:
 a,b=map(int,input().split())
 g[a].append(b)
 g[b].append(a)
visited=[0 for i in range(n+1)]
s=[(k, 0)]
while s:
 q,p=s.pop(-1)
 visited[q]=1
 for nbr in g[q]: 
  if not visited[nbr]:s.append((nbr,q))
  elif nbr!=p and nbr==k:print('NO');exit()
print('YES')