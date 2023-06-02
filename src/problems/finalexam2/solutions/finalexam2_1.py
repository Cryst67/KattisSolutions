n = int(input())
op = []
for i in range(n):
    op.append(input())
score = 0
for i in range(n-1):
    if op[i] == op[i+1]:
        score+=1
print(score)