n = int(input())
for _ in range(n):
    s = input()
    s = list(s[::-1])
    for i in range(len(s)):
        if i % 2 == 0:
            s[i] = int(s[i])
            continue
        c = int(s[i]) * 2
        while c > 9: c = sum(list(map(int, list(str(c)))))
        s[i] = c
    print('PASS' if sum(s) % 10 == 0 else 'FAIL')