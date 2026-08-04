def solution(lines):
    answer = 0
    # 음수는 - 100 으로 처리
    a_list = [0] * 201
    # 겹치면 +1 하기
    for dots in lines:
        for i in range(dots[0], dots[1]):
            a_list[i] += 1
    
    for idx, x in enumerate(a_list):
        if x >= 2:
            # print(idx)
            answer +=1 
    return answer