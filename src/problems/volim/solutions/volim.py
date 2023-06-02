seconds = 210
s = 0
start = int(input())
t = int(input())
for _ in range(t):
    seconds, tf = input().split()
    s += int(seconds)
    if s > 210:
        break
    if tf != 'T':
        continue
    start += 1
start = 8 if start % 8 == 0 else start % 8
print(start)