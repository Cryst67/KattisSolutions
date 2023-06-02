l=[70,21,42,63,14,35,56,7,28,49]
for _ in range(int(input())):
 n = int(input())
 if n>=l[n%10]: print(l[n%10]//7)
 else: print(-1)