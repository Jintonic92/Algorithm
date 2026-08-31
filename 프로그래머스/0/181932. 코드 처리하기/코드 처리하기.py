def solution(code):
    answer = ''
    
    mode = '0' 
    
    for idx, v in enumerate(code):
        # print(mode, idx, v)
        
        if mode == '0':
            if v != '1':
                if idx % 2 == 0:
                    answer += v
            else:
                mode = '1'
        
        else: 
            if v != '1':
                if idx % 2 == 1:
                    answer += v
            else:
                mode = '0'
        
    if len(answer) == 0:
        return "EMPTY"
                    
    return answer