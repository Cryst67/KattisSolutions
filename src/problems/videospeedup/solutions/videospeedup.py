n, p, k = map(int, input().split())
time = 0
speed = 1
times = set(map(int, input().split()))
for i in range(1, k+1):
    time += speed
    if i in times: speed += (p/100)
print(time)