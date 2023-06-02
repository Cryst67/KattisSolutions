tasks, time = map(int, input().split())
times = list(map(int, input().split()))
count = 0
for t in times:
    if time - t < 0 :
        break
    time -= t
    count += 1
print(count)