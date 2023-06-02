n, a, b, c = map(int, input().split())
dp = [[0 for i in range(n)] for i in range(3)]
key = [a, b, c]
dp[0][0] = a; dp[1][0] = b; dp[2][0] = c
for c in range(1, n):
    for r in range(3):
        for rr in range(3):
            if r == rr: continue
            dp[r][c] += dp[rr][c-1] * key[r]
        dp[r][c] %= (1000000000 + 7)
res = 0
for i in range(3):
    res += dp[i][n-1]
print(res % (1000000000 + 7))