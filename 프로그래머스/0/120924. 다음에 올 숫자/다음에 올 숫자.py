def solution(common):
    answer = 0
    # 등차수열
    
    if common[1] - common[0] == common[2] - common[1] :
        return common[-1] + common[1] - common[0]
    
    else: 
        diff = common[1] // common[0]
        return common[0] * diff**len(common)
    return answer