w = int(input())
n = int(input())

areas = 0
for i in range(n):
    wi, li = map(int, input().split())
    areas += (wi * li)

print(int(areas/w))