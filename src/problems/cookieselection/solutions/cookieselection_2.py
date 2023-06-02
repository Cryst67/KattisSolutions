from heapq import heappop, heappush
h1 = []
h2 = []
n = 0
while True:
    try: s = input()
    except EOFError: break
    if s == '#': 
        if n % 2 != 0:
            print(-1 * heappop(h1))
        else:
            print(heappop(h2))
        n -= 1
        if n < 0: n = 0
        continue
    s = int(s)
    n += 1
    if len(h1) == 0:
        heappush(h1, -1 * s)
        continue
    if len(h2) == 0:
        h1_top = heappop(h1)
        if -1 * h1_top >= s:
            heappush(h2, -1 * h1_top)
            heappush(h1, -1 * s)
        else:
            heappush(h2, s)
            heappush(h1, h1_top)
        continue
    h1_top = heappop(h1)
    h2_top = heappop(h2)
    if s <= -1 * h1_top:
        heappush(h1, -1 * s)
    else: heappush(h2, s)
    heappush(h1, h1_top)
    heappush(h2, h2_top)
    if len(h2) > len(h1):
        h2_top = heappop(h2)
        heappush(h1, -1 * h2_top)
    if len(h1) > len(h2) + 1:
        heappush(h2, -heappop(h1))