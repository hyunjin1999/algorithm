li = [list(map(int, input().split())) for _ in range(9)]

maximum = -99
ans1 = 0
ans2 = 0

for idx1, x in enumerate(li):
    for idx2, y in enumerate(x):
        if y > maximum:
            maximum = y
            ans1 = idx1
            ans2 = idx2

print(maximum)
print(ans1+1, ans2+1)