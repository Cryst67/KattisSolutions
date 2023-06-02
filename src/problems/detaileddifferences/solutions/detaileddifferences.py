n = int(input())

for i in range(n):
    a = input()
    b = input()
    s = ""
    for j in range(len(a)):
        if a[j] == b[j]:
            s += '.'
        else: s += '*'
    print(a)
    print(b)
    print(s)
    print()