def convert(n, q):
    if n == 0:
        return '0'
    
    base = ''
    num = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    # n을 q진수로 변환
    while n > 0:
        n, mod = divmod(n, q)
        if mod > 9:
            base += str(num[mod])
        else:
            base += str(mod)

    return base[::-1]
    
    
def solution(n, t, m, p):
    answer = ''
    current_num = 0 # 현재 숫자
    order = 1       # 차례
    
    while len(answer) < t:
        # print(len(answer), answer)
        # 해당 진법으로 숫자 변환
        convert_num = convert(current_num, n)
        print(convert_num)
        for num in convert_num:
            if len(answer) >= t: break
            
            # 하남자 차례일 때
            if order % m == p or (p == m and order % m == 0):
                answer += num
            
            order += 1
        current_num += 1
                
    return answer