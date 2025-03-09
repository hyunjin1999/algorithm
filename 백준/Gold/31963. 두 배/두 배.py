n = int(input())
nums = list(map(int, input().split()))
current = nums[0]
ans = 0
for i in range(1, len(nums)):
    while nums[i-1] > nums[i]:
        nums[i] = nums[i] * 2
        ans += 1
        
print(ans)