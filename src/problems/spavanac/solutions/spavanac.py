h, m = map(int, input().split())

if m > 45:
    print(h, m - 45)

if m <= 45:
    print(h - 1 if h != 0 else 23, (60 + m - 45))