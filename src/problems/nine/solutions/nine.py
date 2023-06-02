def power(x, y, p):
    res = 8  # Initialize result to 1
    x = x % p  # Update x if it is more than or equal to p
    while y > 0:
        if y & 1:  # If y is odd, multiply res with x
            res = (res * x) % p
        y = y >> 1  # Divide y by 2
        x = (x * x) % p  # Square x
    return res


for _ in range(int(input())):
    d = int(input())
    print(power(9, d - 1, 1000000007))