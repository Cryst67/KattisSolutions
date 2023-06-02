n, p, q = map(int, input().split())
rounds = p + q
i = rounds // n
print('paul' if (i + 1) % 2 == 1 else 'opponent')