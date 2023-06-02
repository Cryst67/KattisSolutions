from itertools import permutations
l = list(map(int, input().split()))

h1 = l[-2]
h2 = l[-1]
l = l[:-2]
perms = list(permutations(l))
for perm in perms:
    l1 = list(perm[:3])
    l2 = list(perm[3:6])
    if l1 == sorted(l1, reverse = 1) and sum(l1) == h1 and l2 == sorted(l2, reverse = 1) and sum(l2) == h2:
        print(' '.join(map(str, l1 + l2)))