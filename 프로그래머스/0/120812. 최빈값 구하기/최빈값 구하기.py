def solution(array):
    a_list = [0] * 1001
    for n in array:
        a_list[n] += 1
    max_x = max(a_list)
    answer = [idx for idx, x in enumerate(a_list) if x == max_x]
    if len(answer) > 1:
        return -1
    else: return answer[0]