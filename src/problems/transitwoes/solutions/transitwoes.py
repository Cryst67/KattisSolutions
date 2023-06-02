s, t, n = map(int, input().split())
transits = list(map(int, input().split()))
times = list(map(int, input().split()))
intervals = list(map(int, input().split()))

all_time = t
cur_time = 0
for i in range(n):
    cur_time += transits[i]
    arrival = intervals[i]
    while cur_time > arrival:
        arrival += intervals[i]
    cur_time+= arrival - cur_time
    cur_time+= times[i]
cur_time+=transits[n]

if (t - s) < cur_time:
    print('no')
    exit()
print('yes')