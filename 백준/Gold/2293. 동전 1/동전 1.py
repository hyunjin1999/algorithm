n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()

prev = [0 for _ in range(k+1)] # 이전 동전의 경우의 수(초기화: 0원으로 만들 수 있는 경우의 수)
curr = [0 for _ in range(k+1)]
prev[0] = 1 # 0원을 만들 수 있는 경우의 수는 항상 1가지

for i in range(n):

    coin = coins[i]
    if coin > k: break
    # print(coin)
    for j in range(coin):
        curr[j] = prev[j]
    for j in range(coin, k+1):
        curr[j] = prev[j] + curr[j - coin]

    prev = curr.copy()

print(curr[-1])