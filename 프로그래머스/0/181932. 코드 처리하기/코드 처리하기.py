def solution(code):
    answer = ''
    
    mode = 0 
    
    for idx, c in enumerate(code):
        if mode == 0:        
            if c != '1':
                if idx % 2 == 0:
                    answer += c
            else:
                mode = 1        
        
        else:
            if c != '1':
                if idx % 2 == 1:
                    answer += c
            else:
                mode = 0
    
    if len(answer) == 0:
        return "EMPTY"
    return answer