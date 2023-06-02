l=[70,21,42,63,14,35,56,7,28,49]
for _ in range(int(input())):
 n=int(input())
 a=n%10
 print(l[a]//7 if n>=l[a] else -1)