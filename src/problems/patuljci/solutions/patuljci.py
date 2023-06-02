nums = []
for i in range(9): nums.append(int(input()))
for i in range(9):
    for j in range(9):
        if i == j: continue
        a = nums.copy()
        a.remove(nums[i])
        a.remove(nums[j])
        if sum(a) == 100:
            for num in a:
                print(num)
            exit()