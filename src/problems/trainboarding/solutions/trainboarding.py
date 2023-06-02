n, l, p = map(int, input().split())
trains = [0] + [l*(i+1) for i in range(n)]
entrances = [(trains[i] + trains[i - 1])/2 for i in range(1, n + 1)]
e_f = dict(zip(entrances, [0 for i in range(n)]))
passengers = [int(input()) for _ in range(p)]
max_dist = float('-inf')
for passenger in passengers:
    dist = float('inf')
    enter = 0
    for entrance in entrances:
        if abs(passenger - entrance) <= dist:
            dist = abs(passenger - entrance)
            enter = entrance
    max_dist = max(max_dist, dist)
    e_f[enter] += 1
maxi = float('-inf')
for key in e_f:
    maxi = max(maxi, e_f[key])
print(int(max_dist))
print(maxi)