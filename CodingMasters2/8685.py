## 8685: 법인등록번호
a = input()
b = input()
c = int(input())
answer = ['X', 'X', 'X', 'X', 'X']

remainder = 10 - c  # 10으로 나눈 나머지
if remainder == 10: remainder = 0
odd, even = 0, 0

for i in range(len(a + b)):
    if i % 2 == 1:  # 0번째가 1번째이다.
        even += int((a + b)[i])
    else:
        odd += int((a + b)[i])


def is_possible(start, end, order):
    for i in range(start, end + 1):
        tmp_odd = str(i)[0]
        tmp_even = str(i)[1]
        if (((2 * (even + int(tmp_even))) + (odd + int(tmp_odd))) % 10) == remainder:
            answer[order] = 'O'
            return


is_possible(11, 15, 0)
is_possible(21, 22, 1)
is_possible(31, 51, 2)
is_possible(81, 86, 3)
is_possible(71, 71, 4)

print(''.join(answer))
