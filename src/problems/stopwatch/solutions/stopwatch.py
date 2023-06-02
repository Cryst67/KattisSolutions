n = int(input())
times = []
for i in range(n):
    times.append(int(input()))
if n % 2 == 1:
    print('still running')
    exit()
time = 0
for i in range(n):
    if i % 2 == 0:
        continue
    time += times[i] - times[i-1]
print(time)
    