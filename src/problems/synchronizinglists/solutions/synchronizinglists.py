abc = []
while True:
    n = int(input())
    if n == 0:
        break
    fl = []
    sl = []
    for i in range(n):
        num = int(input())
        fl.append(num)
    for i in range(n):
        num = int(input())
        sl.append(num)
    original = fl.copy()
    fl.sort()
    sl.sort()
    final = []
    for i in range(n):
        final.append(sl[fl.index(original[i])])
        sl.remove(sl[fl.index(original[i])])
        fl.remove(original[i])
    abc.append(final)
for i in range(len(abc)):
    for j in range(len(abc[i])):
        print(abc[i][j])
    if i != len(abc) -1:
        print()