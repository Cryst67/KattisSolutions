n = int(input())
o = [0 for i in range(n)]
o[0] = 1
l = list(map(int, input().split()))
for i in range(n - 1):
    o[l[i] + 1] = i + 2
for num in o:
    print(num, end=' ')
print()