import random
def is_prime(n, k=5):
    if n==2 or n == 3:return True
    if n < 2 or n % 2 == 0:return False
    r, s = 0, n-1
    while s % 2 == 0:
        r += 1
        s //= 2
    # Perform k rounds of the Miller-Rabin test
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
    case, n = map(int, input().split())
    visited = set([n])
    if not is_prime(n):
        print(case, n, 'NO')
        continue
    happy = 0
    cur = n
    while True:
        new_n = sum(list(map(lambda x: int(x) ** 2, list(str(cur)))))
        if new_n in visited:
            break
        visited.add(new_n)
        if new_n == 1: happy = 1; break
        cur = new_n
    if happy:
        print(case, n, 'YES')
    else: print(case, n, 'NO')

