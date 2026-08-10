def solution(common):
    answer = 0
    # 등비|등차
    if common[1] - common[0] == common[2] - common[1]:
        answer += common[-1] + common[1] - common[0]
    else:
        n = common[1] // common[0]
        answer = common[-1] * n
    return answer
