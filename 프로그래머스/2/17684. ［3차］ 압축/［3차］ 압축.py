def solution(msg):
    answer = []
    
    lzw = {}
    alpha = 65
    for i in range(1, 27):
        lzw[chr(alpha)] = i
        alpha += 1

    dict_idx = 27
    
    current_input = ''
    for m in msg:
        current_input += m
        if current_input in lzw.keys():
            continue
        else:
            answer.append(lzw[current_input[:-1]])
            lzw[current_input] = dict_idx
            dict_idx += 1
            current_input = m
            
    answer.append(lzw[current_input])

    return answer