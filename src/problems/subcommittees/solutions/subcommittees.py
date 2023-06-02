n = int(input())
l = set()
for i in range(1, int(n **.5) + 1):
 if n % i == 0:l.add(i);l.add(n//i)
l =sorted(list(l))
i = 1
c = 1
while n != 1:
 if n % l[i] == 0: n//=l[i];c += 1
 else: i += 1
print(c)