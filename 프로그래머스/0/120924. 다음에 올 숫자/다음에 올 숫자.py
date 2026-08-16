def solution(common):
    answer = 0
    

    if common[1] - common[0] == common[2] - common[1]:
        diff = common[1] - common[0]
        answer = common[-1] + diff
    
    else:
        diff = common[1] // common[0]
        answer = common[-1] * diff

    return answer