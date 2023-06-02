n, m = map(int, input().split())
s = set()
for i in range(1, n+1): s.add(i)
v = [0 for i in range(m)]
for i in range(m):
    num = int(input())
    v[i] = num
    s.remove(num)
s = list(s)
index = 0
while index < len(v):
    while s and s[0] < v[index]:
        print(s[0])
        s.remove(s[0])
    print(v[index])
    index +=1

while s:
    print(s[0])
    s.remove(s[0])