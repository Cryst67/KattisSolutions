while True:
    n = int(input())
    if n == -1:
        break
    distance = 0
    prev = 0
    for i in range(n):
        s, t = map(int, input().split())
        distance += s * (t - prev)
        prev = t
    print(f"{distance} miles")