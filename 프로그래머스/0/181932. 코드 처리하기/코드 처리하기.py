def solution(code):
    answer = ''
    curr_mode = '0'
    
    for idx, c in enumerate(code):
        #print("current_mode", curr_mode, "idx", idx, "c", c)
        if c == '1':
            curr_mode = '1' if curr_mode == '0' else '0'
            continue
            
        if curr_mode == '0' :
            if idx % 2 == 0 :
                answer += c
        else:
            if idx % 2 == 1 :
                answer += c
    if len(answer) == 0:
        return "EMPTY"
    return answer

