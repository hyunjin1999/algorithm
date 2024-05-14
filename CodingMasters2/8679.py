## 8679: 채터링
n, k = map(int, input().split())
cmd = input()
answer = ''
for c in cmd:
    answer += (c * k)

print(answer)