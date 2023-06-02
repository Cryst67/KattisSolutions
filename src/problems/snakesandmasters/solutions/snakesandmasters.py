def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b % 10**6, (a + b) % 10**6
    return b

def count_ways(n):
    return fibonacci(n + 1)
print(count_ways(int(input())))