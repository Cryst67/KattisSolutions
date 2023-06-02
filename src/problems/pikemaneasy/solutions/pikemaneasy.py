n, t = map(int, input().split())
a, b, c, t0 = map(int, input().split())
times = [t0]
for i in range(1, n):
    times += [((a * times[i - 1] + b) % c) + 1]
times.sort()
total_time = 0
penalty = 0
count= 0
i = 0
while i < n and total_time + times[i] <= t:
    total_time += times[i]
    penalty += total_time 
    penalty %= int(1e9+7)
    count+=1
    i += 1
print(count, penalty)