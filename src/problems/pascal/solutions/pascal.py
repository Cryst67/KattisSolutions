n = int(input())
c = 0
if n == 1: print(0)
else:
    found = 0
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            found = 1
            print(n - n//i)
            break
    if not found:
        print(n - 1)