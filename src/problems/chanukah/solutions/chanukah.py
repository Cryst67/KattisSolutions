n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    days = b * (1 + b)/2 + b
    print(a, int(days))