n = int(input())
distances = [*map(int, input().split())]
s = set()
sm = sum(distances)
for i in range(n):
    s.add(sm - distances[i])
s = sorted(list(s))
print(len(s))
print(' '.join(map(str, s)))