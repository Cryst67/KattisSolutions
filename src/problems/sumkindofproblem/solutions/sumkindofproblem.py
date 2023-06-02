for i in range(int(input())):
    case, n = map(int, input().split())
    odd, even, pos = 0, 0, 0
    oddsum, evensum, possum = 0, 0, 0
    cur = 1
    while odd < n or even < n or pos < n:
        if pos < n:
            possum += cur
            pos += 1
        if odd < n and cur % 2 == 1:
            oddsum += cur
            odd += 1
        if even < n and cur % 2 == 0:
            evensum += cur
            even += 1
        cur += 1
    print(case, possum, oddsum, evensum)