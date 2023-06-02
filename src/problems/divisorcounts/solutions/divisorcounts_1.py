def find_divisors(N):
    divisors = [0] * (N+1)

    for i in range(1, N+1):
        for j in range(i, N+1, i):
            divisors[j] += 1

    return divisors[1:]

N = int(input())
divisors = find_divisors(N)

for d in divisors:
    print(d)
