import math

n = int(input())
nums = list(map(int, input().split()))
current = nums[0]
ans = 0
for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        temp =  math.ceil(math.log2(nums[i-1] / nums[i]))
        ans += temp
        nums[i] = nums[i] * (2 ** temp)
        
print(ans)