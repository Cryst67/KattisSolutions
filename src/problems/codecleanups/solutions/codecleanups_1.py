n = int(input())
days = set(list(map(int, input().split())))
dirty_pushes = []
j = 0
cleanups = 0

for i in range(1, 366):
    if i in days:
        dirty_pushes += [0]
    s = sum(map(lambda x : x + 1, dirty_pushes), 0)
    if s < 20:
        dirty_pushes = list(map(lambda x : x + 1, dirty_pushes))
        continue
    else:
        cleanups += 1
        dirty_pushes.clear()
if dirty_pushes:
    cleanups += 1
print(cleanups)
