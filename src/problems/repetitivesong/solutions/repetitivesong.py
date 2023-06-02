prev = {}
final = {}
n = int(input())
for i in range(n):
    w = input()
    if w not in prev:
        prev[w] = i
        continue
    if w not in final:
        final[w] = abs(i - prev[w])
    else:
        final[w] = min(final[w], i - prev[w])
    prev[w] = i
mini = float('inf')
for key in final:
    mini = min(final[key], mini)
if mini == float('inf'): print(0);exit()
print(n - mini)