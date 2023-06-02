n = input()
sum = 0
a = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
sum = 0
flag = False
for i in range(len(n)):
    if n[i] == '-':
        flag = True
        continue
    if flag:
        sum+= int(n[i])*a[i - 1]
        continue
    sum+= int(n[i])*a[i]

print(1 if sum % 11 == 0 else 0)
