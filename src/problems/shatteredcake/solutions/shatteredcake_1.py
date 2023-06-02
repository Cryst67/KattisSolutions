import sys
lines = sys.stdin.readlines()
w = int(lines[0])
n = int(lines[1])

areas = 0
for i in range(2, n + 2):
    wi, li = map(int, lines[i].split())
    areas += (wi * li)

print(int(areas/w))