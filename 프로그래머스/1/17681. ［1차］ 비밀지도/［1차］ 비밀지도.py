def solution(n, arr1, arr2):
    answer = []
    map = []
    for i in range(n):
        temp = (bin(arr1[i] | arr2[i])[2:])
        if len(temp) != n:
            plus_str = '0' * (n - len(temp))
            temp = plus_str + temp
        map.append(temp)
        
    
    for m in map:
        m = m.replace('1', '#')
        answer.append(m.replace('0', ' '))
    
    return answer