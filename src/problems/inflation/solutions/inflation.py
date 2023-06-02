n = int(input())
l = sorted(list(map(int, input().split())))
flag = 0
mini = 1
for i in range(n):
    if l[i] > i + 1:
        flag = 1
        break
    mini = min(mini, l[i]/(i+1))
print(mini if not flag else 'impossible')