while True:
    n = int(input())
    if n == 0: break
    nums = []
    b = list(reversed(bin(n - 1)[2:]))
    for i in range(len(b)):
        if b[i] == '1':
            nums.append(3 ** (i))
    final = ', '.join(map(str, nums))
    print(f'{{ {final} }}')