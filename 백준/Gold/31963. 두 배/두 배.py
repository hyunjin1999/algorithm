import math
N = int(input())
arr = list(map(int, input().split()))

rst = 0
cnt = [0] * N

for i in range(1, N):
    log_rst = math.log2(arr[i - 1] / arr[i])
    temp = math.ceil(log_rst) + cnt[i - 1]
    if temp > 0:
        cnt[i] = temp
        rst += cnt[i]

print(rst)