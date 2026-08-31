
def solution(array):
    answer = []
    a_list = [0] * 1001
    for a in array:
        a_list[a] += 1
    
    max_a = max(a_list)
    
    for idx, a in enumerate(a_list):
        if a == max_a:
            answer.append(idx)

    if len(answer) > 1:
        return -1
    
    return answer[0]