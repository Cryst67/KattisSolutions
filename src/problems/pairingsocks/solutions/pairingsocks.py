n = int(input())
l = list(reversed([*map(int, input().split())]))
stack = []
for i in range(2*n - 1, -1, -1):
    if len(stack) == 0:
        stack.append(l[i])
        l.pop()
        continue
    if stack[-1] == l[i]:
        stack.pop()
        l.pop()
    else: 
        stack.append(l.pop())
if stack or l: print('impossible')
else: print(2*n)