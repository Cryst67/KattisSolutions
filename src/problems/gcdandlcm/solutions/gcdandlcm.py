import math

def find_pairs(x, y):
    pairs = []
    lcm_x = y // x
    for i in range(1, int(math.sqrt(lcm_x)) + 1):
        if lcm_x % i == 0:
            j = lcm_x // i
            if math.gcd(i, j) == 1:
                pairs.append((i * x, j * x))
                if i != j:
                    pairs.append((j * x, i * x))
    return sorted(pairs)

x, y = map(int, input().split())
pairs = find_pairs(x, y)

for pair in pairs:
    print(pair[0], pair[1])