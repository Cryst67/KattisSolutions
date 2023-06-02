def get_clock_angle(h, m):
    hr = (h + m/60) * 30
    mn = m * 6
    if hr < mn:
        return abs(mn - hr)
    if mn < hr:
        return 360 - abs(mn - hr)
def get_time(angle):
    for i in range(1, 13):
        for j in range(0,61):
            a = get_clock_angle(i, j)
            if a < 0: a = 360 + a
            if a == angle/10: return i, j

h, m = get_time(int(input()))
print(f"{h:02d}:{m:02d}")