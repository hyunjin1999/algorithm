n, l = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n):
    same_count = 1  # 같은 높이가 나온 횟수
    prev = li[i][0]  # 이전 높이
    is_possible = True

    for j in range(1, n):

        # 이전 높이와 현재 높이가 같을 떼
        if li[i][j] == prev:
            same_count += 1

        # 이전 높이와 현재 높이가 다를 때
        else:

            # 이전 높이와 현재 높이가 1 이상 차이날 때
            if abs(li[i][j] - prev) > 1:
                is_possible = False
                break

            # 이전 높이보다 한 칸 내려간 경우
            elif prev > li[i][j]:
                if j + l <= n and li[i][j: j+l].count(li[i][j]) >= l:
                    is_possible = True
                    prev = li[i][j]
                    same_count = -l + 1
                else:
                    is_possible = False
                    break

            # 이전 높이보다 한 칸 올라간 경우
            elif prev < li[i][j]:

                # 같은 높이가 나온 횟수가 경사로 밑면 길이보다 크거나 같을 때
                if same_count >= l:
                    is_possible = True
                    same_count = 1
                    prev = li[i][j]

                # 같은 높이가 나온 횟수가 경사로 밑면 길이보다 작을 때
                else:
                    is_possible = False
                    break

    if is_possible:
        answer += 1


for i in range(n):
    same_count = 1  # 같은 높이가 나온 횟수
    prev = li[0][i]  # 이전 높이
    is_possible = True

    for j in range(1, n):

        # 이전 높이와 현재 높이가 같을 떼
        if li[j][i] == prev:
            same_count += 1

        # 이전 높이와 현재 높이가 다를 때
        else:

            # 이전 높이와 현재 높이가 1 이상 차이날 때
            if abs(li[j][i] - prev) > 1:
                is_possible = False
                break

            # 이전 높이보다 한 칸 내려간 경우
            elif prev > li[j][i]:
                if j + l <= n:
                    count = 0
                    for temp in range(l):
                        if li[j + temp][i] == li[j][i]: count += 1
                    if count == l:
                        is_possible = True
                        prev = li[j][i]
                        same_count = -l + 1
                    else:
                        is_possible = False
                        break
                else:
                    is_possible = False
                    break

            # 이전 높이보다 한 칸 올라간 경우
            elif prev < li[j][i]:

                # 같은 높이가 나온 횟수가 경사로 밑면 길이보다 크거나 같을 때
                if same_count >= l:
                    is_possible = True
                    same_count = 1
                    prev = li[j][i]

                # 같은 높이가 나온 횟수가 경사로 밑면 길이보다 작을 때
                else:
                    is_possible = False
                    break

    if is_possible:
        answer += 1

print(answer)
