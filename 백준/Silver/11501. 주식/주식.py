def cal(li):
    # print('또', li)
    s = sum(li[:-1])
    # print('여기',(li[-1] * (len(li) - 1)) - s)
    return (li[-1] * (len(li) - 1)) - s


t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    answer = 0

    sp = len(prices) - 1
    cur_max = -99
    for i in range(sp, -1, -1):
        if cur_max < prices[i]:
            cur_max = prices[i]
        elif cur_max > prices[i]:
            answer += (cur_max - prices[i])

    print(answer)