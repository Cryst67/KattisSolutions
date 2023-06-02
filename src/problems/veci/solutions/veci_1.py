from itertools import permutations
n = input()
perm = permutations(list(n))
mini = float('inf')
best = None
for i in list(perm):
    num = int(''.join(i))
    if num > int(n):
        if num - int(n) < mini:
            best = num
            mini = num - int(n)
print(0 if best is None else best)
