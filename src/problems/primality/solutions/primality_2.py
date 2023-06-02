import random

def is_prime(n, k=5):
    """Return True if n is a probable prime, False if it is composite."""
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    # Find r and s such that n-1 = 2^s * r, where r is odd
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

print('YES' if is_prime(int(input()))else 'NO')