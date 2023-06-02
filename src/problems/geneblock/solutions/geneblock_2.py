l=[70,21,42,63,14,35,56,7,28,49]
for _ in range(int(input())):
 n=int(input())
 a=n%10
 if n>=l[a]:print(l[a]//7)
 else: print(-1)