from math import factorial as f
END = 1e9
n = int(input())
a,c = 0, lambda n, r: f(n)//(f(r)*f(n - r))
for i in range(n, 0, -1):
    combinations = c(n, i)
    permutations = combinations*f(i)
    a += permutations
print('JUST RUN!!' if a > END else a)