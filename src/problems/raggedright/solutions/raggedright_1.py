lines = []
n = float('-inf')
while True:
    try:
        line = input()
        n = max(n, len(line))
        lines.append(line)
    except EOFError: break
penalty = 0
for i in range(len(lines) - 1):
    if len(lines[i]) > n: continue
    penalty += (n - len(lines[i])) ** 2
print(penalty)