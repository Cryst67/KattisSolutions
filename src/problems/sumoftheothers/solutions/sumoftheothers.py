while True:
    try:
        nums = list(map(int, input().split()))
    except EOFError:
        break
    for i in range(len(nums)):
        pos_sum = nums[i]
        rest_sum = 0
        for j in range(len(nums)):
            if i == j:
                continue
            rest_sum+=nums[j]
        if pos_sum == rest_sum:
            print(pos_sum)
            break