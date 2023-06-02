n, r, k = map(int, input().split())
steps = k
steps += abs(r - k)
steps_left = max(0, n - steps)
if steps_left % 2 == 0:
    steps += steps_left
    steps += r
else:
    steps += steps_left
    steps += r + 1
print(steps)