n = int(input())
l = list(map(int, input().split()))
gis = [l[0]]
for i in range(1, n):
    if l[i] > gis[-1]: gis += [l[i]]
print(len(gis))
print(' '.join(map(str, gis)))