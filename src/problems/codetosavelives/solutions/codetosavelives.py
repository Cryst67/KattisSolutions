for _ in range(int(input())):
    a = int(input().replace(' ', ''))
    b = int(input().replace(' ', ''))
    ans = list(str(a + b))
    for n in ans:
        print(n, end=' ')