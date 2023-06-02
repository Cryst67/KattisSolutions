import sys
import random
input = sys.stdin.readline
def is_prime(n, k=5):
    if n==2 or n == 3:return True
    if n < 2 or n % 2 == 0:return False
    r, s = 0, n-1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n-1)
        x = pow(a, s, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True

for i in range(int(input())):
    n = int(input())
    f = []
    for j in range(2, n//2 + 1):
        if is_prime(j) and is_prime(n - j):
            f += [(j, n - j)]
    print(f'{n} has {len(f)} representation(s)')
    for pair in f:
        print('+'.join(map(str, pair)))
    print()
