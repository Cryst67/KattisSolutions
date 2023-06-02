n, m = map(int, input().split())
l = [0 for i in range(n + 1)]
for i in range(m):
    a = int(input())
    l[a] = a
if m == n: print('too late');exit()
for i in range(1 , n + 1):
    if l[i] == 0:
        print(i)
        break

