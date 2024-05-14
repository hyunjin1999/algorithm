## 8687: 전화번호 입력
number = input()
number = number.split('-')
if number[0] != '010':
    print('invalid')
    exit()
elif (len(number[1]) != 4) or (len(number[2]) != 4):
    print('invalid')
    exit()
else:
    print('valid')