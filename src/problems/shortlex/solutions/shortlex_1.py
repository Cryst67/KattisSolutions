def get_shortlex_number(n):
    alphabet = ["0", "1"]
    shortlex = ""
    while n > 0:
        index = (n - 1) % 2
        shortlex = alphabet[index] + shortlex
        n = (n - 1) // 2
    return shortlex

n = int(input())
for _ in range(n):
    print(get_shortlex_number(int(input())))