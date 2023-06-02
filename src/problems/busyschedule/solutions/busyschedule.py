d = {}
def get_military_time(time):
    t, b = time.split()
    h, m = t.split(':')
    if b == 'a.m.':
        h = str(int(h) % 12)
    if b == 'p.m.':
        h = str((int(h) % 12) + 12)
    t = h + m
    t = int(t)
    return t

from heapq import heappop, heappush
while True:
    t = int(input())
    if t == 0: break
    h = []
    for i in range(t):
        time = input()
        mil_time = get_military_time(time)
        if mil_time not in d:
            d[mil_time] = time
        heappush(h, mil_time)
    while h:
        print(d[heappop(h)])