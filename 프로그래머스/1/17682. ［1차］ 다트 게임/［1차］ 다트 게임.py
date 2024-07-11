def solution(dartResult):
    results = [0, 0, 0]
    current_idx = -1
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    for idx, r in enumerate(dartResult):
        if r.isdecimal():
            if r == '1' and dartResult[idx+1] == '0':
                continue
            if idx != 0 and r == '0' and dartResult[idx-1] == '1':
                current_idx += 1
                results[current_idx] += 10
                continue
            current_idx += 1
            results[current_idx] += int(r)
        else:
            if r == 'S' or r == 'D' or r == 'T':
                results[current_idx] = results[current_idx] ** bonus[r]
                
            # 스타상, 아차상인 경우
            else:
                if r == '*':
                    if current_idx == 0:
                        results[current_idx] = results[current_idx] * 2
                    else:
                        results[current_idx] = results[current_idx] * 2
                        results[current_idx - 1] = results[current_idx - 1] * 2
                else:
                    results[current_idx] = -results[current_idx]    
    print(results)
    return sum(results)