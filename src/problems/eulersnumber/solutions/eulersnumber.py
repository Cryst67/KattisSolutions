memo = [0 for i in range(10001)]
def factorial(n):
    if n == 0:
        memo[0] = 1
        return memo[n]
    if memo[n] != 0:
        return memo[n]
    memo[n] = n * factorial(n - 1)
    return memo[n]

n = int(input())
e = 0
for i in range(n + 1):
    e += 1/factorial(i)
print(e)