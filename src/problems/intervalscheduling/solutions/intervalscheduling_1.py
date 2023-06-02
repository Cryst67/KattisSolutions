import sys
input = sys.stdin.readline
n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
intervals.sort(key = lambda x: x[1])
count = 0
prev = 0
for interval in intervals:
    if interval[0] >= prev:
        count += 1
        prev = interval[1]
print(count)