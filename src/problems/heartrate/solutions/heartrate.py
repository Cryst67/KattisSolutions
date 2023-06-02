n = int(input())

for i in range(n):
    b, p = map(float, input().split())
    bpm = 60 * b/p
    diff = bpm/b
    print(bpm - diff, bpm, bpm + diff)
    