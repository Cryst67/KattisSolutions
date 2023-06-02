import math
 
def is_prime(n: int) -> bool:
    # Check if n=1 or n=0
    if n <= 1:
        return False
    # Check if n=2 or n=3
    if n == 2 or n == 3:
        return True
    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check from 5 to square root of n
    # Iterate i by (i+6)
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
 
    return True
 
print('YES' if is_prime(int(input()))else 'NO')