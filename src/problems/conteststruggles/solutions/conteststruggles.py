n, k = map(int, input().split())
all_avg, lotte_avg = map(int, input().split())

final = (all_avg * n - lotte_avg * k)/(n - k)
print(final if final >= 0 and final <= 100 else 'impossible')