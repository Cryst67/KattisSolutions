n = int(input())
nums = []
for i in range(n):
    nums.append((input()))
    
sum = 0
for i in range(n):
    sum += int(nums[i][0:-1]) ** int(nums[i][-1])
print(sum)