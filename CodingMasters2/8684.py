## 8684 문제: 삼색잉크
# 입력 받기
start_week = input()
num = int(input())
holiday = []
for i in range(num):
    temp = list(map(int, input().split()))
    holiday.append(temp)

# 휴일 정렬
holiday = sorted(holiday)
holiday.append([99, 99])

# 횟수를 저장할 변수
count = {}
for i in range(10):
    count[i] = [0, 0, 0]  # 빨, 파, 검

# 말일
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 0월, 1월, 2월 ...

# 요일
week = {'SUN': 0, 'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6}

# 현재 요일
current_week = week[start_week]

for idx, month in enumerate(days):
    for day in range(1, month+1):
        temp = list(str(day))
        if (idx == holiday[0][0]) and (day == holiday[0][1]):  # 공휴일인 경우
            for i in temp:
                count[int(i)][0] += 1
            holiday.pop(0)
        elif current_week == 0:  # 일요일인 경우
            for i in temp:
                count[int(i)][0] += 1
        elif current_week == 6:  # 토요일인 경우
            for i in temp:
                count[int(i)][1] += 1
        else:  # 평일인 경우
            for i in temp:
                count[int(i)][2] += 1
        current_week = (current_week + 1) % 7

for value in count.values():
    value = list(map(str, value))
    print(' '.join(value))
