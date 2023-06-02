n = int(input())
w_in = list(map(int, input().split()))
cost = 0
index = 0
mini = float('inf')
for i in range(n):
    if w_in[i] < mini:
        mini = w_in[i]
        index = i
for i in range(n):
    if i == index:
        continue
    cost += w_in[i] + mini
    
print(cost)