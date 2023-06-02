
n = int(input())
l = list(map(int, input().split()))

a = [[l[0]]]
index = 0
for i in range(1, n):
    flag = False
    if l[i] <= a[index][-1]:
        a.append([l[i]])
        Flag = True
        index += 1
    else:
        for j in range(len(a)):
            if l[i] > a[j][-1]:
                a[j].append(l[i])
                flag = True
                break
print(len(a))
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()
