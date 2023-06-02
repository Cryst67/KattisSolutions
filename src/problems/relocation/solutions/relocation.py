n, q = map(int, input().split())
locations = list(map(int, input().split()))
for i in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        locations[b - 1] = c
    if a == 2:
        print(abs(locations[b - 1] - locations[c - 1]))